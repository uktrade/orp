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


def calculate_score(search_result, search_terms):
    """
    Calculate the score of a search result based on the number of
    search terms found in the title and description.

    :param search_result: A dictionary containing the search result.
    :param search_terms: A list of search terms to look for in the
                         search result.
    :return: The score based on the number of search terms found.
    """
    title = search_result.get("title", "") or ""
    description = search_result.get("description", "") or ""
    combined_content = title.lower() + " " + description.lower()
    score = sum(combined_content.count(term.lower()) for term in search_terms)
    return score
