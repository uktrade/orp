import logging

import pandas as pd
import requests  # type: ignore

from jinja2 import Template
from orp_search.config import SearchDocumentConfig
from orp_search.dummy_data import get_construction_data_as_dataframe

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

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

    def finalise_results(
        self, config: SearchDocumentConfig, results, context
    ) -> dict:
        """
        Paginates the given search results based on the provided configuration.

        Arguments:
         config (SearchDocumentConfig): Configuration parameters for search,
                                        including pagination limits.
         results: A collection of search results to be paginated.
         context: A dictionary containing context data which will be updated
                  with pagination details.

        Returns:
         A tuple containing:
          - Updated context dictionary with pagination information.
          - Paginator instance used for paginating the results.

        The context dictionary is updated with the following keys:
         is_paginated: A boolean indicating if the results span multiple pages.
         reports: The paginated results for the current page.
         paginator: The Paginator instance.
         page_obj: The current page of results.
        """
        paginator = Paginator(results, config.limit)
        try:
            paginated_documents = paginator.page(config.offset)
        except PageNotAnInteger:
            paginated_documents = paginator.page(1)
        except EmptyPage:
            paginated_documents = paginator.page(paginator.num_pages)

        # Iterate over each document in paginated_documents
        if paginated_documents:
            for paginated_document in paginated_documents:
                if "description" in paginated_document:
                    paginated_document["description"] = (
                        paginated_document["description"][:100] + "..."
                        if len(paginated_document["description"]) > 100
                        else paginated_document["description"]
                    )
                if "regulatory_topics" in paginated_document:
                    paginated_document["regulatory_topics"] = str(
                        paginated_document["regulatory_topics"]
                    ).split("\n")

        # Pass the paginated results to the template
        context["paginator"] = paginator
        context["is_paginated"] = paginator.num_pages > 1
        context["results"] = paginated_documents
        context["results_count"] = len(paginated_documents)
        context["results_total_count"] = paginator.count
        context["results_page_total"] = paginator.num_pages
        context["current_page"] = config.offset
        return context

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
                logger.info(
                    "publisher_terms_pattern: %s", publisher_terms_pattern
                )
                filtered_df = filtered_df[
                    filtered_df["publisher_id"].str.contains(
                        publisher_terms_pattern, case=True, na=False
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

            if config.sort_by == "recently":
                # Sort the DataFrame by 'date_modified' in descending order
                # Ensure 'date_issued' is in datetime format
                filtered_df["date_issued"] = pd.to_datetime(
                    filtered_df["date_issued"], format="%d/%m/%Y"
                )

                # Sort the DataFrame by 'date_issued' in descending order
                sorted_df = filtered_df.sort_values(
                    by="date_issued", ascending=False
                )
            elif config.sort_by == "relevance":
                # Calculate relevance score
                # (based on the number of keywords found)
                def calculate_relevance(row, search_terms):
                    def score_text(text, terms):
                        text_processed = text.replace(" ", "").lower()
                        return sum(
                            1
                            for term in terms
                            if term.replace(" ", "").lower() in text_processed
                        )

                    title_score = score_text(row["title"], search_terms)
                    description_score = score_text(
                        row["description"], search_terms
                    )
                    return title_score + description_score

                filtered_df["relevance_score"] = filtered_df.apply(
                    calculate_relevance,
                    axis=1,
                    search_terms=config.search_terms,
                )

                # Sort the DataFrame by 'relevance_score' in descending order
                sorted_df = filtered_df.sort_values(
                    by="relevance_score", ascending=False
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
