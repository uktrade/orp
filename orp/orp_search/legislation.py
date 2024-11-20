import base64
import logging
import xml.etree.ElementTree as ET  # nosec BXXX

from typing import Optional

import requests  # type: ignore

from orp_search.config import SearchDocumentConfig
from orp_search.construction_legislation import (  # noqa: E501
    construction_legislation_dataframe,
)
from orp_search.utils.date import convert_date_string_to_obj
from orp_search.utils.documents import (  # noqa: E501
    generate_short_uuid,
    insert_or_update_document,
)

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


def _get_text_from_element(element: Optional[ET.Element]) -> Optional[str]:
    return element.text if element is not None else None


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

    def build_cache(self, config: SearchDocumentConfig):
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
                    identifier = _get_text_from_element(
                        root.find(".//dc:identifier", self._namespaces)
                    )  # nosec BXXX
                    title = _get_text_from_element(
                        root.find(".//dc:title", self._namespaces)
                    )  # nosec BXXX
                    description = _get_text_from_element(
                        root.find(".//dc:description", self._namespaces)
                    )  # nosec BXXX
                    format = _get_text_from_element(
                        root.find(".//dc:format", self._namespaces)
                    )  # nosec BXXX
                    language = _get_text_from_element(
                        root.find(".//dc:language", self._namespaces)
                    )  # nosec BXXX
                    publisher = _get_text_from_element(
                        root.find(".//dc:publisher", self._namespaces)
                    )  # nosec BXXX
                    modified = _get_text_from_element(
                        root.find(".//dc:modified", self._namespaces)
                    )  # nosec BXXX
                    valid = _get_text_from_element(
                        root.find(".//dct:valid", self._namespaces)
                    )  # nosec BXXX

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
                raise e

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
            "id": generate_short_uuid(),
            "title": title,
            "identifier": identifier,
            "publisher": publisher,
            "language": language if language is not None else "eng",
            "format": format if format is not None else "",
            "description": description if description is not None else "",
            "date_issued": convert_date_string_to_obj(modified),
            "date_modified": convert_date_string_to_obj(modified),
            "date_valid": valid,
            "sort_date": convert_date_string_to_obj(valid),
            "type": "Legislation",
            "score": 0,
        }
