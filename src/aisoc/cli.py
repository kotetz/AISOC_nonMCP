"""Command-line entry point: `aisoc <command> ...` (or `python -m aisoc ...`).

This is the only interface Copilot Skills should call into. Every subcommand
is read-only and goes through the guardrailed `run_kql` primitive.
"""
from __future__ import annotations

import argparse
import sys

from . import formatting
from .clients import incidents as incidents_client
from .clients.logs import run_kql
from .guardrails import DEFAULT_HOURS, MAX_HOURS, MAX_ROWS


def _cmd_query(args: argparse.Namespace) -> None:
    rows = run_kql(args.kql, hours=args.hours, max_rows=args.max_rows)
    print(formatting.to_json(rows))
    if len(rows) >= args.max_rows:
        print(f"# NOTE: results truncated at {args.max_rows} rows.", file=sys.stderr)


def _cmd_incident_get(args: argparse.Namespace) -> None:
    incident = incidents_client.get_incident(args.number)
    print(formatting.format_incident(incident))


def _cmd_incident_alerts(args: argparse.Namespace) -> None:
    alerts = incidents_client.list_alerts(args.number)
    print(formatting.format_alerts(alerts))


def _cmd_incident_entities(args: argparse.Namespace) -> None:
    entities = incidents_client.list_entities(args.number)
    print(formatting.format_entities(entities))


def _cmd_triage(args: argparse.Namespace) -> None:
    severities = args.severity.split(",") if args.severity else None
    open_incidents = incidents_client.list_open_incidents(hours=args.hours, severities=severities)
    print(formatting.format_incident_list(open_incidents))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="aisoc", description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    p_query = sub.add_parser("query", help="Run an ad-hoc KQL query")
    p_query.add_argument("kql", help="KQL query text")
    p_query.add_argument(
        "--hours",
        type=int,
        default=DEFAULT_HOURS,
        help=(
            f"Lookback window in hours (default {DEFAULT_HOURS} = 7 days). "
            f"Raise up to {MAX_HOURS} ({MAX_HOURS // 24} days, the workspace's "
            "retention ceiling) if you suspect a longer-running compromise."
        ),
    )
    p_query.add_argument(
        "--max-rows", type=int, default=MAX_ROWS, help=f"Row cap (default {MAX_ROWS})"
    )
    p_query.set_defaults(func=_cmd_query)

    p_incident = sub.add_parser("incident", help="Incident lookups")
    incident_sub = p_incident.add_subparsers(dest="incident_command", required=True)

    p_get = incident_sub.add_parser("get", help="Show incident details")
    p_get.add_argument("number", type=int, help="IncidentNumber")
    p_get.set_defaults(func=_cmd_incident_get)

    p_alerts = incident_sub.add_parser("alerts", help="List alerts linked to an incident")
    p_alerts.add_argument("number", type=int, help="IncidentNumber")
    p_alerts.set_defaults(func=_cmd_incident_alerts)

    p_entities = incident_sub.add_parser("entities", help="List entities linked to an incident")
    p_entities.add_argument("number", type=int, help="IncidentNumber")
    p_entities.set_defaults(func=_cmd_incident_entities)

    p_triage = sub.add_parser("triage", help="List and rank currently open incidents")
    p_triage.add_argument(
        "--hours", type=int, default=24 * 30, help="Lookback window in hours (default 720)"
    )
    p_triage.add_argument("--severity", help="Comma-separated severity filter, e.g. High,Medium")
    p_triage.set_defaults(func=_cmd_triage)

    return parser


def _force_utf8_output() -> None:
    """Force UTF-8 stdout/stderr regardless of the OS console code page.

    Incident/alert titles pulled from Sentinel commonly contain characters
    (e.g. en-dashes, curly quotes) that are not representable in the Windows
    default console encoding (cp932/cp1252), which would otherwise crash
    `print()` with a UnicodeEncodeError.
    """
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace")


def main(argv: list[str] | None = None) -> int:
    _force_utf8_output()
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        args.func(args)
    except Exception as exc:  # surfaced to the calling agent as a readable error
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
