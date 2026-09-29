"""KQL-based helpers for retrieving Microsoft Sentinel incidents, alerts, and
entities.

Everything here goes through the same read-only Log Analytics Query API used
by `run_kql` (via `SecurityIncident` / `SecurityAlert`); there is no dependency
on the Microsoft.SecurityInsights ARM API, which keeps authentication to a
single scope and this tool's surface area small.
"""
from __future__ import annotations

import json
from typing import Any

from ..guardrails import LOOKUP_MAX_HOURS
from .logs import run_kql

_SEVERITY_RANK = {"High": 3, "Medium": 2, "Low": 1, "Informational": 0}


def _parse_dynamic(value: Any) -> Any:
    """Best-effort parse of a KQL `dynamic` column value returned as JSON text."""
    if isinstance(value, (list, dict)) or value is None:
        return value
    if isinstance(value, str):
        try:
            return json.loads(value)
        except ValueError:
            return value
    return value


def get_incident(incident_number: int) -> dict[str, Any] | None:
    """Return the latest known snapshot of a Sentinel incident by its number."""
    query = (
        "SecurityIncident "
        f"| where IncidentNumber == {int(incident_number)} "
        "| order by TimeGenerated desc "
        "| take 1"
    )
    rows = run_kql(query, hours=LOOKUP_MAX_HOURS, hours_ceiling=LOOKUP_MAX_HOURS, max_rows=1)
    if not rows:
        return None
    incident = rows[0]
    incident["AlertIds"] = _parse_dynamic(incident.get("AlertIds"))
    incident["Labels"] = _parse_dynamic(incident.get("Labels"))
    return incident


def list_alerts(incident_number: int) -> list[dict[str, Any]]:
    """Return the SecurityAlert rows linked to an incident's AlertIds."""
    incident = get_incident(incident_number)
    if not incident or not incident.get("AlertIds"):
        return []
    alert_ids = ", ".join(f"'{a}'" for a in incident["AlertIds"])
    query = (
        "SecurityAlert "
        f"| where SystemAlertId in ({alert_ids}) "
        "| project TimeGenerated, AlertName, AlertSeverity, Description, "
        "Tactics, Techniques, ProductName, Entities "
        "| order by TimeGenerated desc"
    )
    alerts = run_kql(query, hours=LOOKUP_MAX_HOURS, hours_ceiling=LOOKUP_MAX_HOURS, max_rows=200)
    for alert in alerts:
        alert["Entities"] = _parse_dynamic(alert.get("Entities"))
    return alerts


def list_entities(incident_number: int) -> dict[str, list[str]]:
    """Group all entities referenced by an incident's alerts by entity type."""
    grouped: dict[str, set[str]] = {}
    for alert in list_alerts(incident_number):
        for entity in alert.get("Entities") or []:
            if not isinstance(entity, dict):
                continue
            etype = entity.get("Type", "Unknown")
            value = (
                entity.get("Name")
                or entity.get("HostName")
                or entity.get("Address")
                or entity.get("Url")
                or entity.get("FileName")
                or entity.get("Value")
                or json.dumps(entity, default=str)
            )
            grouped.setdefault(etype, set()).add(str(value))
    return {etype: sorted(values) for etype, values in grouped.items()}


def list_open_incidents(
    hours: int = 24 * 30, severities: list[str] | None = None
) -> list[dict[str, Any]]:
    """Return open (New/Active) incidents, ranked by a simple priority heuristic."""
    query = (
        "SecurityIncident "
        "| summarize arg_max(TimeGenerated, *) by IncidentNumber "
        '| where Status in ("New", "Active")'
    )
    incidents = run_kql(query, hours=hours, hours_ceiling=LOOKUP_MAX_HOURS, max_rows=2000)

    for incident in incidents:
        incident["AlertIds"] = _parse_dynamic(incident.get("AlertIds"))

    if severities:
        wanted = {s.strip().title() for s in severities}
        incidents = [i for i in incidents if i.get("Severity") in wanted]

    def _priority(incident: dict[str, Any]) -> tuple[int, int]:
        severity_score = _SEVERITY_RANK.get(incident.get("Severity"), 0)
        alert_count = len(incident.get("AlertIds") or [])
        return (severity_score, alert_count)

    return sorted(incidents, key=_priority, reverse=True)
