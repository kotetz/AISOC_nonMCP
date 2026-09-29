"""Unit tests for clients.incidents. All Azure calls are mocked via run_kql;
no network access or real credentials are required to run these tests.
"""
from unittest.mock import patch

from aisoc.clients import incidents

SAMPLE_INCIDENT_ROW = {
    "IncidentNumber": 123,
    "Title": "Test incident",
    "Severity": "High",
    "Status": "New",
    "AlertIds": '["alert-1", "alert-2"]',
    "Labels": None,
}

SAMPLE_ALERT_ROWS = [
    {
        "TimeGenerated": "2026-01-01T00:00:00Z",
        "AlertName": "Suspicious sign-in",
        "AlertSeverity": "High",
        "Entities": '[{"Type": "Account", "Name": "jdoe"}, {"Type": "IP", "Address": "1.2.3.4"}]',
    }
]


@patch("aisoc.clients.incidents.run_kql")
def test_get_incident_parses_dynamic_columns(mock_run_kql):
    mock_run_kql.return_value = [dict(SAMPLE_INCIDENT_ROW)]

    incident = incidents.get_incident(123)

    assert incident["AlertIds"] == ["alert-1", "alert-2"]
    mock_run_kql.assert_called_once()


@patch("aisoc.clients.incidents.run_kql")
def test_get_incident_returns_none_when_missing(mock_run_kql):
    mock_run_kql.return_value = []

    assert incidents.get_incident(999) is None


@patch("aisoc.clients.incidents.run_kql")
def test_list_alerts_filters_by_alert_ids(mock_run_kql):
    mock_run_kql.side_effect = [
        [dict(SAMPLE_INCIDENT_ROW)],
        [dict(row) for row in SAMPLE_ALERT_ROWS],
    ]

    alerts = incidents.list_alerts(123)

    assert alerts[0]["Entities"][0]["Type"] == "Account"
    assert "alert-1" in mock_run_kql.call_args_list[1].args[0]


@patch("aisoc.clients.incidents.run_kql")
def test_list_alerts_returns_empty_without_alert_ids(mock_run_kql):
    mock_run_kql.return_value = [{**SAMPLE_INCIDENT_ROW, "AlertIds": None}]

    assert incidents.list_alerts(123) == []


@patch("aisoc.clients.incidents.run_kql")
def test_list_entities_groups_by_type(mock_run_kql):
    mock_run_kql.side_effect = [
        [dict(SAMPLE_INCIDENT_ROW)],
        [dict(row) for row in SAMPLE_ALERT_ROWS],
    ]

    entities = incidents.list_entities(123)

    assert entities["Account"] == ["jdoe"]
    assert entities["IP"] == ["1.2.3.4"]


@patch("aisoc.clients.incidents.run_kql")
def test_list_open_incidents_filters_and_ranks_by_severity(mock_run_kql):
    mock_run_kql.return_value = [
        {"IncidentNumber": 1, "Severity": "Low", "Status": "New", "AlertIds": "[]"},
        {"IncidentNumber": 2, "Severity": "High", "Status": "New", "AlertIds": '["a", "b"]'},
        {"IncidentNumber": 3, "Severity": "Medium", "Status": "Active", "AlertIds": '["a"]'},
    ]

    ranked = incidents.list_open_incidents()

    assert [i["IncidentNumber"] for i in ranked] == [2, 3, 1]


@patch("aisoc.clients.incidents.run_kql")
def test_list_open_incidents_applies_severity_filter(mock_run_kql):
    mock_run_kql.return_value = [
        {"IncidentNumber": 1, "Severity": "Low", "Status": "New", "AlertIds": "[]"},
        {"IncidentNumber": 2, "Severity": "High", "Status": "New", "AlertIds": "[]"},
    ]

    ranked = incidents.list_open_incidents(severities=["high"])

    assert [i["IncidentNumber"] for i in ranked] == [2]
