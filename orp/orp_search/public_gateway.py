import json
import logging

from datetime import datetime

import requests  # type: ignore

from orp_search.utils.documents import insert_or_update_document

logger = logging.getLogger(__name__)


def _normalize_date(date_str):
    if date_str is None:
        return None

    # If the date is in YYYY format, add "-01-01"
    if len(date_str) == 4:
        return f"{date_str}-01-01"
    # If the date is in YYYY-MM format, add "-01"
    elif len(date_str) == 7:
        return f"{date_str}-01"
    # Otherwise, assume the date is already in YYYY-MM-DD format
    return datetime.strptime(date_str, "%Y-%m-%d").strftime("%Y-%m-%d")


def _build_like_conditions(field, and_terms, or_terms):
    """

    Generates SQL LIKE conditions.

    Args:
        field (str): The database field to apply the LIKE condition to.
        terms (list of str): A list of terms to include in the LIKE
                             condition.

    Returns:
        str: A string containing the LIKE conditions combined with 'OR'.
    """
    # Put each term into the list
    terms = and_terms

    # If there are OR terms, then put an OR condition between them
    if or_terms:
        terms.append("(" + " OR ".join(or_terms) + ")")

    return " OR ".join([f"{field} LIKE LOWER('%{term}%')" for term in terms])


class PublicGateway:
    def __init__(self):
        """
        Initializes the API client with the base URL for the Trade Data API.

        Attributes:
            base_url (str): The base URL of the Trade Data API.
        """
        self._base_url = (
            "https://data.api.trade.gov.uk/v1/datasets/orp-regulations"
            "/versions/v1.0.0/data"
        )

    def build_cache(self, config):
        logger.info("fetching all data from orpd...")

        # URL encode the query for the API request
        params = {"format": "json"}

        # Make the GET request
        response = requests.get(
            self._base_url,
            params=params,
            timeout=config.timeout,  # nosec BXXX
        )

        # Check if the request was successful
        if response.status_code == 200:
            data = json.loads(response.text)

            # Now you can use `data` as a usual Python dictionary
            # Convert each row into DataResponseModel object
            total_documents = len(data.get("uk_regulatory_documents"))
            count = 0
            for row in data.get("uk_regulatory_documents"):
                logger.info(
                    f"inserting or updating document {count} /"
                    f"({total_documents})..."
                )
                insert_or_update_document(row)
                count += 1
        else:
            logger.error(
                f"error fetching data from orpd: {response.status_code}"
            )
            return
