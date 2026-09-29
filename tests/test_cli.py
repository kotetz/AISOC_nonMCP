from aisoc.cli import build_parser


def test_query_command_parses_hours_and_max_rows():
    args = build_parser().parse_args(["query", "SecurityIncident | take 1", "--hours", "48"])
    assert args.kql == "SecurityIncident | take 1"
    assert args.hours == 48


def test_incident_get_subcommand():
    args = build_parser().parse_args(["incident", "get", "123"])
    assert args.number == 123
    assert args.incident_command == "get"


def test_incident_alerts_subcommand():
    args = build_parser().parse_args(["incident", "alerts", "123"])
    assert args.number == 123
    assert args.incident_command == "alerts"


def test_triage_default_hours():
    args = build_parser().parse_args(["triage"])
    assert args.hours == 24 * 30
    assert args.severity is None


def test_triage_with_severity_filter():
    args = build_parser().parse_args(["triage", "--severity", "High,Medium"])
    assert args.severity == "High,Medium"
