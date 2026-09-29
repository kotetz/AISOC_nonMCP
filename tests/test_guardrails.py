from aisoc.guardrails import DEFAULT_HOURS, MAX_HOURS, clamp_hours, validate_query
import pytest


def test_clamp_hours_default_on_zero():
    assert clamp_hours(0) == DEFAULT_HOURS


def test_clamp_hours_default_on_negative():
    assert clamp_hours(-5) == DEFAULT_HOURS


def test_clamp_hours_caps_at_ceiling():
    assert clamp_hours(999_999) == MAX_HOURS


def test_clamp_hours_respects_custom_ceiling():
    assert clamp_hours(999_999, ceiling=24 * 365) == 24 * 365


def test_clamp_hours_passes_through_within_ceiling():
    assert clamp_hours(48) == 48


def test_validate_query_rejects_empty():
    with pytest.raises(ValueError):
        validate_query("   ")


def test_validate_query_rejects_control_commands():
    with pytest.raises(ValueError):
        validate_query(".show tables")


def test_validate_query_accepts_normal_kql():
    validate_query("SecurityIncident | take 10")  # should not raise
