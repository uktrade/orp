import logging

import requests  # type: ignore

from jinja2 import Template
from orp_search.config import SearchDocumentConfig
from orp_search.dummy_data import get_construction_data_as_dataframe

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

    def paginate_results(self, config: SearchDocumentConfig, results):
        """
        Paginates the search results.

        Args:
            results (list): The search results to paginate.

        Returns:
            list: The paginated search results.
            count: Total number of pages from results
        """
        start = (config.offset - 1) * config.limit
        end = start + config.limit
        return results[start:end]

    def calculate_total_pages(self, config, results_count):
        """
        Calculates the total number of pages for pagination.

        Args:
            total_results (int): The total number of search results.
            limit (int): The number of results per page.

        Returns:
            int: The total number of pages.
        """
        if config.limit <= 0:
            raise ValueError("limit must be greater than 0")
        return (results_count + config.limit - 1) // config.limit

    def search(self, config: SearchDocumentConfig):
        # List of search terms
        title_search_terms = config.search_terms
        document_type_terms = config.document_types

        # If the dummy flag is set, return dummy data. Ideally, this will be
        # removed from the final implementation
        if config.dummy:
            df = get_construction_data_as_dataframe()

            if config.id:
                logger.info("using dummy data")

                # Fetch the record with the specified id
                record = df[df["id"] == config.id].to_dict(orient="records")
                if record:
                    return record[0]  # Return the first matching record
                else:
                    return None  # Return None if no matching record is found

            search_terms_pattern = "|".join(title_search_terms)

            # Filter the DataFrame based on the search terms
            filtered_df = df[
                (
                    df["title"].str.contains(
                        search_terms_pattern, case=False, na=False
                    )
                )
                & (
                    df["description"].str.contains(
                        search_terms_pattern, case=False, na=False
                    )
                )
            ]

            # If config.publisher_terms is not None, then add filter
            # for publisher in filtered_df
            if config.publisher_terms is not None:
                publisher_terms_pattern = "|".join(config.publisher_terms)
                filtered_df = filtered_df[
                    filtered_df["publisher"].str.contains(
                        publisher_terms_pattern, case=False, na=False
                    )
                ]

            # If config.document_types is not None, then add filter
            # for document types in filtered_df
            if document_type_terms is not None:
                document_type_terms_pattern = "|".join(document_type_terms)
                filtered_df = filtered_df[
                    filtered_df["type"].str.contains(
                        document_type_terms_pattern, case=False, na=False
                    )
                ]

            if config.sort_by is None:
                results = filtered_df.to_dict(orient="records")
                logger.info("filtered data: %s", results)
                return results

            sorted_df = None

            if config.sort_by == "recently_updated":
                # Sort the DataFrame by 'date_modified' in descending order
                sorted_df = filtered_df.sort_values(
                    by="date_modified", ascending=False
                )

            elif config.sort_by == "recently_published":
                # Sort the DataFrame by 'date_issued' in descending order
                sorted_df = filtered_df.sort_values(
                    by="date_issued", ascending=False
                )

            if sorted_df is not None:
                results = sorted_df.to_dict(orient="records")
            else:
                results = []

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
        # summary_conditions = self._build_like_conditions(
        #     "b.summary", summary_search_terms
        # )

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
            # summary_conditions=summary_conditions,
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
