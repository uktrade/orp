from datetime import datetime, timezone

import dateutil.parser  # type: ignore


def parse_date(date_value):
    if isinstance(date_value, datetime):
        if date_value.tzinfo is None:
            # If the datetime is offset-naive, make it offset-aware in UTC
            return date_value.replace(tzinfo=timezone.utc)
        return date_value
    if isinstance(date_value, str):
        try:
            dt = dateutil.parser.parse(date_value)
            if dt.tzinfo is None:
                # If parsed datetime is offset-naive,
                # make it offset-aware in UTC
                return dt.replace(tzinfo=timezone.utc)
            return dt
        except ValueError:
            return None
    return None  # Return None for invalid date types
