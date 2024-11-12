import base64
import logging
import xml.etree.ElementTree as ET  # nosec BXXX

from datetime import datetime

import requests  # type: ignore

from numpy.f2py.auxfuncs import throw_error
from orp_search.config import SearchDocumentConfig
from orp_search.construction_legislation import (  # noqa: E501
    construction_legislation_dataframe,
)
from orp_search.utils.documents import insert_or_update_document

logger = logging.getLogger(__name__)


def _encode_url(url):
    encoded_bytes = base64.urlsafe_b64encode(url.encode("utf-8"))
    return encoded_bytes.decode("utf-8")


def _get_url_data(config, url):
    try:
        response = requests.get(url, timeout=config.timeout)  # nosec BXXX
        if response.status_code == 200:
            return response.text

        # If the status code is not 200, log the error
        logger.error(
            f"error fetching legislation data "
            f"[{response.status_code}]: {response.reason}"
        )
        return None
    except requests.exceptions.RequestException as e:
        logger.error(f"error fetching legislation data: {e}")
        return e


class Legislation:
    def __init__(self):
        # Define the XML namespaces
        self._namespaces = {
            "leg": "http://www.legislation.gov.uk/namespaces/legislation",
            "dc": "http://purl.org/dc/elements/1.1/",
            "dct": "http://purl.org/dc/terms/",
            "atom": "http://www.w3.org/2005/Atom",
            "ukm": "http://www.legislation.gov.uk/namespaces/metadata",
        }

    def build_cache(self):
        logger.info("building legislation cache...")
        dataset = construction_legislation_dataframe()

        # For each row, get the URL from the column named
        # 'URI to Extract XML Data'
        # and store the XML data in a list
        for index, row in dataset.iterrows():
            url = row["URI to Extract XML Data"]
            logger.info(
                f"fetching data from page {index + 1} / "
                f"{len(dataset)}: {url}..."
            )

            try:
                config = SearchDocumentConfig(search_query="", timeout=10)
                data = _get_url_data(config, url)

                if data is None:
                    logger.error(
                        f"error fetching data from {url}. no data returned"
                    )
                    raise Exception(
                        f"error fetching data from {url}. no data returned"
                    )

                if data:
                    logger.info(f"parsing data from {url}...")
                    root = ET.fromstring(data)  # nosec BXXX
                    identifier = root.find(
                        ".//dc:identifier", self._namespaces
                    ).text  # nosec BXXX
                    title = root.find(
                        ".//dc:title", self._namespaces
                    ).text  # nosec BXXX
                    description = root.find(
                        ".//dc:description", self._namespaces
                    ).text  # nosec BXXX
                    format = root.find(
                        ".//dc:format", self._namespaces
                    ).text  # nosec BXXX
                    language = root.find(
                        ".//dc:language", self._namespaces
                    ).text  # nosec BXXX
                    publisher = root.find(
                        ".//dc:publisher", self._namespaces
                    ).text  # nosec BXXX
                    modified = root.find(
                        ".//dc:modified", self._namespaces
                    ).text  # nosec BXXX
                    valid = root.find(
                        ".//dct:valid", self._namespaces
                    ).text  # nosec BXXX

                    document_json = self._to_json(
                        description,
                        format,
                        identifier,
                        language,
                        modified,
                        publisher,
                        title,
                        valid,
                    )

                    # Insert or update the document
                    insert_or_update_document(document_json)
            except Exception as e:
                logger.error(f"error fetching data from {url}: {e}")
                throw_error(f"error fetching data from {url}: {e}")

    def _to_json(
        self,
        description,
        format,
        identifier,
        language,
        modified,
        publisher,
        title,
        valid,
    ):
        return {
            "query": {"search_terms": []},
            "id": _encode_url(identifier),
            "title": title,
            "identifier": identifier,
            "publisher": publisher,
            "language": language,
            "format": format,
            "description": description,
            "date_issued": datetime.strptime(modified, "%Y-%m-%d").strftime(
                "%Y-%m-%d"
            ),
            "date_modified": datetime.strptime(modified, "%Y-%m-%d").strftime(
                "%Y-%m-%d"
            ),
            "date_valid": datetime.strptime(valid, "%Y-%m-%d").strftime(
                "%Y-%m-%d"
            ),
            "type": "legislation",
            "score": 0,
        }
