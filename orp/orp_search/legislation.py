import base64
import logging
import xml.etree.ElementTree as ET  # nosec BXXX

from datetime import datetime

import pandas as pd
import requests  # type: ignore

from orp_search.utils.documents import insert_or_update_document

logger = logging.getLogger(__name__)


def _encode_url(url):
    encoded_bytes = base64.urlsafe_b64encode(url.encode("utf-8"))
    return encoded_bytes.decode("utf-8")


class Legislation:
    def _get_url_data(self, url, config=None):
        try:
            response = requests.get(  # nosec BXXX
                url, timeout=10 if not config.timeout else config.timeout
            )
            if response.status_code == 200:
                return response.text
            return None
        except requests.exceptions.RequestException as e:
            logger.error(f"error fetching legislation data: {e}")
            return None

    def parse_dataset_and_store(self):
        # Read construction_legislation.xlsx into panda
        dataset = pd.read_excel("construction_legislation.xlsx")

        # For each row, get the URL from the column named
        # 'URI to Extract XML Data'
        # and store the XML data in a list
        xml_data = []
        for index, row in dataset.iterrows():
            url = row["URI to Extract XML Data"]
            data = self._get_url_data(url)
            if data:
                xml_data.append(data)

        # For each xml_data parse the XML data but extracting the
        # following fields and store the data in a dictionary and
        # the key should be identifier

        # Define the XML namespaces
        namespaces = {
            "leg": "http://www.legislation.gov.uk/namespaces/legislation",
            "dc": "http://purl.org/dc/elements/1.1/",
            "dct": "http://purl.org/dc/terms/",
            "atom": "http://www.w3.org/2005/Atom",
            "ukm": "http://www.legislation.gov.uk/namespaces/metadata",
        }

        for data in xml_data:
            root = ET.fromstring(data)  # nosec BXXX
            identifier = root.find(
                ".//dc:identifier", namespaces
            ).text  # nosec BXXX
            title = root.find(".//dc:title", namespaces).text  # nosec BXXX
            description = root.find(
                ".//dc:description", namespaces
            ).text  # nosec BXXX
            format = root.find(".//dc:format", namespaces).text  # nosec BXXX
            language = root.find(
                ".//dc:language", namespaces
            ).text  # nosec BXXX
            publisher = root.find(
                ".//dc:publisher", namespaces
            ).text  # nosec BXXX
            modified = root.find(
                ".//dc:modified", namespaces
            ).text  # nosec BXXX
            valid = root.find(".//dct:valid", namespaces).text  # nosec BXXX

            document_data = {
                "id": _encode_url(identifier),
                "title": title,
                "identifier": identifier,
                "publisher": publisher,
                "language": language,
                "format": format,
                "description": description,
                "date_issued": datetime.strptime(
                    modified, "%Y-%m-%d"
                ).strftime("%Y-%m-%d"),
                "date_modified": datetime.strptime(
                    modified, "%Y-%m-%d"
                ).strftime("%Y-%m-%d"),
                "date_valid": datetime.strptime(valid, "%Y-%m-%d").strftime(
                    "%Y-%m-%d"
                ),
                "type": "legislation",
                "coverage": "gb",
                "audience": None,
                "subject": None,
                "license": None,
                "regulatory_topics": None,
                "status": None,
                "date_uploaded_to_orp": None,
                "has_format": None,
                "is_format_of": None,
                "has_version": None,
                "is_version_of": None,
                "references": None,
                "is_referenced_by": None,
                "has_part": None,
                "is_part_of": None,
                "is_replaced_by": None,
                "replaces": None,
                "related_legislation": None,
                "score": 0,
            }

            # Insert or update the document
            insert_or_update_document(document_data)
