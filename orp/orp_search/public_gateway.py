import logging

import pandas as pd
import requests  # type: ignore

from jinja2 import Template
from orp_search.config import SearchDocumentConfig

logger = logging.getLogger(__name__)


class PublicGateway:
    def __init__(self):
        """
        Initializes the API client with the base URL for the Trade Data API.

        Attributes:
            base_url (str): The base URL of the Trade Data API.
        """
        self.base_url = "https://data.api.trade.gov.uk"

    def _build_like_conditions(self, field, terms):
        """

        Generates SQL LIKE conditions.

        Args:
            field (str): The database field to apply the LIKE condition to.
            terms (list of str): A list of terms to include in the LIKE
                                 condition.

        Returns:
            str: A string containing the LIKE conditions combined with 'OR'.
        """
        return " OR ".join([f"{field} LIKE '%{term}%'" for term in terms])

    def search(self, config: SearchDocumentConfig):
        # List of search terms
        title_search_terms = config.search_terms
        summary_search_terms = config.search_terms

        # If the dummy flag is set, return dummy data. Ideally, this will be
        # removed from the final implementation
        if config.dummy:
            df = pd.read_csv("orp/orp_search/construction-data.csv")
            server_terms_pattern = "|".join(title_search_terms)
            document_types_pattern = "|".join(summary_search_terms)
            logger.info("server_terms_pattern: %s", server_terms_pattern)
            logger.info("document_types_pattern: %s", document_types_pattern)

            # Filter the DataFrame based on the search terms
            filtered_df = df[
                (
                    df["title"].str.contains(
                        server_terms_pattern, case=False, na=False
                    )
                )
                & (
                    df["description"].str.contains(
                        document_types_pattern, case=False, na=False
                    )
                )
            ]
            results = filtered_df.to_dict(orient="records")
            logger.info("filtered data: %s", results)
            return results

        # Base URL for the API
        # TODO: need to use aws parameter store to store the base url
        url = (
            "https://data.api.trade.gov.uk/v1/datasets/market-barriers"
            "/versions/v1.0.10/data"
        )

        # Build the WHERE clause
        # TODO: need to use aws parameter store to store the field names
        title_conditions = self._build_like_conditions(
            "b.title", title_search_terms
        )
        summary_conditions = self._build_like_conditions(
            "b.summary", summary_search_terms
        )

        # SQL query to filter based on title and summary containing search
        # terms
        # TODO: we are using example data here, this needs to be updated with
        #  the actual table and field names
        query_template = """
            SELECT *
            FROM S3Object[*].barriers[*] b
            WHERE ({{ title_conditions }}) AND ({{ summary_conditions }})
        """

        template = Template(query_template)
        query = template.render(
            title_conditions=title_conditions,
            summary_conditions=summary_conditions,
        )

        # URL encode the query for the API request
        params = {"format": "json", "query-s3-select": query}

        # Log the query with parameters
        logger.info("request will contain the following query: %s", query)
        logger.info(
            "request will contain the following parameters: %s", params
        )

        # Make the GET request
        response = requests.get(url, params=params, timeout=config.timeout)

        # Check if the request was successful
        if response.status_code == 200:
            data = response.text
            logger.info("data fetched successfully: %s", data)
            return data
        else:
            logger.error("data fetch failed: %s", response.text)
            return None
