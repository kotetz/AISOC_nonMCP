"""Thin wrapper around the Azure Monitor Log Analytics Query API.

This is the single primitive every other client and every Skill ultimately
calls. Keeping all data access behind one function makes the guardrails
(time-span clamp, row cap, timeout) impossible to bypass accidentally.
"""
from __future__ import annotations

import sys
from datetime import timedelta
from typing import Any

from azure.monitor.query import LogsQueryClient, LogsQueryStatus

from ..auth import get_credential
from ..config import get_settings
from ..guardrails import DEFAULT_HOURS, MAX_HOURS, MAX_ROWS, SERVER_TIMEOUT_SECONDS, clamp_hours, validate_query

_client: LogsQueryClient | None = None


def _get_client() -> LogsQueryClient:
    global _client
    if _client is None:
        _client = LogsQueryClient(get_credential())
    return _client


def run_kql(
    query: str,
    hours: int = DEFAULT_HOURS,
    max_rows: int = MAX_ROWS,
    hours_ceiling: int = MAX_HOURS,
) -> list[dict[str, Any]]:
    """Execute a KQL query against the configured workspace and return rows as dicts.

    Args:
        query: KQL query text. Constructed by the caller/Skill at investigation
            time -- this tool intentionally has no library of canned queries.
        hours: Requested lookback window in hours.
        max_rows: Client-side cap on the number of rows returned.
        hours_ceiling: Upper bound `hours` is clamped to. Internal callers that
            filter on an exact key (e.g. IncidentNumber) may pass a much larger
            ceiling since such queries stay cheap regardless of time span.
    """
    validate_query(query)
    settings = get_settings()
    client = _get_client()

    response = client.query_workspace(
        settings.workspace_id,
        query,
        timespan=timedelta(hours=clamp_hours(hours, ceiling=hours_ceiling)),
        server_timeout=SERVER_TIMEOUT_SECONDS,
    )

    if response.status == LogsQueryStatus.SUCCESS:
        tables = response.tables
    elif response.status == LogsQueryStatus.PARTIAL:
        print(f"# WARNING: partial results ({response.partial_error})", file=sys.stderr)
        tables = response.partial_data
    else:
        raise RuntimeError(f"Query failed with status: {response.status}")

    rows: list[dict[str, Any]] = []
    for table in tables:
        for row in table.rows:
            rows.append(dict(zip(table.columns, row)))
            if len(rows) >= max_rows:
                return rows
    return rows
