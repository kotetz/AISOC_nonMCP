"""Safety limits applied to every KQL query executed by this tool.

The Log Analytics Query API is inherently read-only (there is no data-plane
write/delete operation exposed by this endpoint), so these guardrails focus on
keeping ad-hoc investigative queries cheap and readable rather than on
preventing data modification.
"""
from __future__ import annotations

DEFAULT_HOURS = 24 * 7  # 1 week: a realistic starting point for investigations,
# not just "the last day" (see below).
MAX_HOURS = 24 * 90  # ceiling for open-ended / ad-hoc exploratory queries.
# This matches this workspace's Log Analytics retention (90 days -- verify with
# `az monitor log-analytics workspace show` if you fork this tool onto a
# different workspace, and adjust to match). Investigations that turn up signs
# of a longer-running compromise (e.g. an identity already flagged
# confirmedCompromised, credential-dumping tooling, unexplained persistence)
# should re-run with `--hours` raised up to this ceiling to find how far back
# the activity actually started. Beyond this ceiling the underlying data has
# been purged by Log Analytics retention and is not recoverable through this
# tool; a true long-term dwell-time hunt would require a separate integration
# with the Microsoft Sentinel data lake (up to 12 years of retention), which is
# intentionally out of scope for this workspace.
LOOKUP_MAX_HOURS = 24 * 365  # ceiling for exact-match lookups against the
# lightweight SecurityIncident/SecurityAlert tables (cheap regardless of span
# because they filter on an exact IncidentNumber/SystemAlertId match). Note
# this only helps for the SecurityIncident row itself (which persists as long
# as it keeps getting touched); the underlying SecurityAlert rows are still
# subject to the same MAX_HOURS-worth of real retention.
MAX_ROWS = 500
SERVER_TIMEOUT_SECONDS = 60

# Control commands (start with a dot, e.g. `.show`, `.set`) operate on workspace
# configuration rather than data. The query endpoint does not execute them
# today, but they are rejected explicitly out of caution.
_BLOCKED_PREFIXES = (".",)


def clamp_hours(hours: int, ceiling: int = MAX_HOURS) -> int:
    """Clamp a requested time span to a sane investigative window."""
    if hours <= 0:
        return DEFAULT_HOURS
    return min(hours, ceiling)


def validate_query(query: str) -> None:
    """Raise ValueError if the query looks empty or like a control command."""
    stripped = query.strip()
    if not stripped:
        raise ValueError("Query must not be empty.")
    if stripped.startswith(_BLOCKED_PREFIXES):
        raise ValueError(
            "Control commands (queries starting with '.') are not allowed. "
            "Use a regular KQL data query instead."
        )
