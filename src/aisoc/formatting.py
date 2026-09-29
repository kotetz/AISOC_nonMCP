"""Human/agent-friendly text rendering for CLI output."""
from __future__ import annotations

import json
from typing import Any, Iterable


def to_json(rows: Iterable[dict[str, Any]]) -> str:
    return json.dumps(list(rows), indent=2, default=str, ensure_ascii=False)


def format_incident(incident: dict[str, Any] | None) -> str:
    if not incident:
        return "Incident not found."
    fields = [
        "IncidentNumber",
        "Title",
        "Severity",
        "Status",
        "Classification",
        "Owner",
        "CreatedTime",
        "LastModifiedTime",
        "Description",
        "IncidentUrl",
    ]
    lines = [f"{f}: {incident.get(f)}" for f in fields if f in incident]
    alert_ids = incident.get("AlertIds") or []
    lines.append(f"AlertCount: {len(alert_ids)}")
    return "\n".join(lines)


def format_alerts(alerts: list[dict[str, Any]]) -> str:
    if not alerts:
        return "No linked alerts found."
    fields = ["TimeGenerated", "AlertName", "AlertSeverity", "ProductName", "Tactics", "Techniques"]
    blocks = ["\n".join(f"{f}: {alert.get(f)}" for f in fields) for alert in alerts]
    return "\n\n".join(blocks)


def format_entities(entities: dict[str, list[str]]) -> str:
    if not entities:
        return "No entities found."
    blocks = [f"{etype} ({len(values)}):\n  " + "\n  ".join(values) for etype, values in entities.items()]
    return "\n\n".join(blocks)


def format_incident_list(incidents: list[dict[str, Any]]) -> str:
    if not incidents:
        return "No open incidents matched the filter."
    lines = []
    for i, incident in enumerate(incidents, start=1):
        alert_count = len(incident.get("AlertIds") or [])
        lines.append(
            f"{i}. [{incident.get('Severity')}] #{incident.get('IncidentNumber')} "
            f"{incident.get('Title')} (Status={incident.get('Status')}, Alerts={alert_count})"
        )
    return "\n".join(lines)
