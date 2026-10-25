from datetime import date
from pipeline_utils import (
    clean_column_name, parse_uk_date, safe_expiry, agent_valid_on
)


def test_clean_column_name_removes_spaces():
    assert clean_column_name("Store Code") == "Store_Code"


def test_clean_column_name_brackets_give_double_underscore():
    assert clean_column_name("RM (Regional Manager)") == "RM__Regional_Manager_"


def test_parse_uk_date():
    assert parse_uk_date("01/01/2025") == date(2025, 1, 1)


def test_safe_expiry_fills_null():
    assert safe_expiry(None) == date(9999, 12, 31)


def test_safe_expiry_keeps_real_date():
    assert safe_expiry(date(2026, 3, 1)) == date(2026, 3, 1)


def test_agent_valid_within_range():
    assert agent_valid_on(date(2025, 6, 1), date(2025, 1, 1), date(2026, 1, 1))


def test_agent_not_valid_before_effective():
    assert not agent_valid_on(date(2024, 12, 31), date(2025, 1, 1), None)


def test_agent_current_record_has_no_expiry():
    assert agent_valid_on(date(2030, 1, 1), date(2025, 1, 1), None)
