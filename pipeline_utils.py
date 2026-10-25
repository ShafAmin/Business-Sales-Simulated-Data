import re
from datetime import datetime, date


def clean_column_name(col_name):
    """Same rule the Bronze/Silver notebooks use for Delta-safe names."""
    return re.sub(r'[ ,;{}()\n\t=]', '_', col_name)


def parse_uk_date(value):
    """Parse dd/MM/yyyy text, as used for Start_Date."""
    return datetime.strptime(value.strip(), "%d/%m/%Y").date()


def safe_expiry(expiry):
    """SCD2: a null expiry date means 'still current' (9999-12-31)."""
    return expiry if expiry is not None else date(9999, 12, 31)


def agent_valid_on(order_date, effective, expiry):
    """True if the agent record was valid on the given date."""
    return effective <= order_date <= safe_expiry(expiry)
