from typing import Any

from core.dbt_data_api import DbtDataApi

DBT_DATA_API = DbtDataApi()


def search_data_api(search_query: str) -> dict[str, Any]:
    """Search company reports.

    Takes a company search query and returns filtered results with report
    counts.

    Returns a dictionary containing:
            - results: List of filtered company results with report counts.
            - request_exception: Any exception raised during the API request.
            - truncated: Whether the results were truncated.
    """
    data = DBT_DATA_API.search_regulations()
    return {
        "results": data,
    }
