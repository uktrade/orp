import base64
import logging

from io import StringIO

import pandas as pd
import requests  # type: ignore

from orp_search.config import SearchDocumentConfig

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

logger = logging.getLogger(__name__)


def _extract_td_value(html_content, target_text):
    # Step 1: Locate the <h2> element and the subsequent <table> element
    h2_text = '<h2 class="title">Count Results</h2>'
    table_class = '<table class="results results-single query-builder"'
    start_index = html_content.find(h2_text)
    if start_index == -1:
        raise ValueError("specified <h2> text not found in the HTML content")

    start_index = html_content.find(table_class, start_index)
    if start_index == -1:
        raise ValueError(
            "specified <table> class not found in the HTML content"
        )

    # Step 2: Locate the <th> tag with the target text
    th_start = html_content.find(f"<th>{target_text}</th>", start_index)
    if th_start == -1:
        raise ValueError(
            f"<th>{target_text}</th> not found in the HTML content"
        )

    # Step 3: Find the <td> tag immediately following the located <th> tag
    td_start = html_content.find("<td>", th_start)
    if td_start == -1:
        raise ValueError("no <td> tag found after the specified <th> tag")

    td_end = html_content.find("</td>", td_start)
    if td_end == -1:
        raise ValueError(
            "No closing </td> tag found after the specified <th> tag"
        )

    # Step 4: Extract and return the content within the <td> tag
    td_value = html_content[  # noqa: E203
        td_start + len("<td>") : td_end  # noqa: E203
    ].strip()  # noqa: E203
    return td_value


def _perform_request(url, params, timeout=10):
    logger.info(f"url for request: {url}")
    logger.info(f"params for request: {params}")
    response = requests.get(url, params=params, timeout=timeout)
    return response.text if response.status_code == 200 else None


def _encode_url(url):
    encoded_bytes = base64.urlsafe_b64encode(url.encode("utf-8"))
    return encoded_bytes.decode("utf-8")


class Legislation:
    def __init__(self):
        self.search_url = (
            "https://research.legislation.gov.uk/query-builder/search/data.csv"
        )
        self.count_url = (
            "https://research.legislation.gov.uk/query-builder/count"
        )

    def search(self, config: SearchDocumentConfig):
        # List of search terms
        title_search_terms = config.search_terms
        search_terms = ",".join(title_search_terms)
        params = {
            "amendments": "include",
            "query": search_terms,
            "count": "100",
        }

        # Get search results
        data_csv = _perform_request(self.search_url, params, config.timeout)

        # Convert the response (string) to a file-like object
        data_io = StringIO(data_csv)

        # Read the CSV string into a DataFrame
        df = pd.read_csv(data_io)

        results = []
        # Convert data_csv into data api format and to list
        for index, item in df.iterrows():
            results.append(
                {
                    "id": _encode_url(item["id"]),
                    "title": item["title"],
                    "document_type": "legislation",
                    "publisher_id": item["type"],
                    "publisher": "UK Legislation",
                    "type": "Legislation",
                    "date_modified": item["valid"],
                }
            )

        logger.info(f"legislation total results: {len(results)}")
        return results

    def finalise_results(
        self, config: SearchDocumentConfig, results, context
    ) -> dict:
        title_search_terms = config.search_terms
        search_terms = ",".join(title_search_terms)
        params = {
            "amendments": "include",
            "query": search_terms,
            # 'counting': 'documents',
        }

        # Get count of total results
        count_data_html_page = _perform_request(
            self.count_url, params, config.timeout
        )
        total_document_count = _extract_td_value(
            count_data_html_page, "documents"
        )

        paginated_documents = []
        exists = False

        # Check if paginator exists in context
        if "paginator" not in context:
            logger.info("paginator not in context for legislation")
            context["paginator"] = {}
            paginator = Paginator(results, config.limit)
            try:
                paginated_documents = paginator.page(config.offset)
            except PageNotAnInteger:
                paginated_documents = paginator.page(1)
            except EmptyPage:
                paginated_documents = paginator.page(paginator.num_pages)
        else:
            logger.info("paginator exists in context for legislation")
            exists = True
            paginator = context["paginator"]

        # If paginator exists then add all results to paginator
        if exists:
            all_items = paginator.object_list

            # Convert to a list if necessary
            all_non_legislation_items = list(all_items)

            # Combine with legislation results
            all_items = all_non_legislation_items + results

            paginator = Paginator(all_items, config.limit)
            try:
                paginated_documents = paginator.page(config.offset)
            except PageNotAnInteger:
                paginated_documents = paginator.page(1)
            except EmptyPage:
                paginated_documents = paginator.page(paginator.num_pages)

        context["paginator"] = paginator
        context["is_paginated"] = paginator.num_pages > 1
        context["results"] = paginated_documents
        context["results_count"] = len(paginated_documents)
        context["results_total_count"] = total_document_count
        context["results_page_total"] = paginator.num_pages
        context["current_page"] = config.offset
        return context
