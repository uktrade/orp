import base64
import logging
import xml.etree.ElementTree as ET  # nosec BXXX

import requests  # type: ignore

from orp_search.config import SearchDocumentConfig

logger = logging.getLogger(__name__)


def _encode_url(url):
    encoded_bytes = base64.urlsafe_b64encode(url.encode("utf-8"))
    return encoded_bytes.decode("utf-8")


class Legislation:
    def __init__(self):
        self.search_url = "https://www.legislation.gov.uk/search"

    def search(self, config: SearchDocumentConfig):
        logger.info("searching legislation...")

        # List of search terms
        title_search_terms = config.search_terms
        search_terms = ",".join(title_search_terms)
        headers = {"Accept": "application/atom+xml"}
        params = {
            "lang": "en",
            "title": search_terms,
            "text": search_terms,
            "results-count": 100,
        }

        # Register namespaces
        ET.register_namespace("", "http://www.w3.org/2005/Atom")
        ET.register_namespace(
            "leg", "http://www.legislation.gov.uk/namespaces/legislation"
        )
        ET.register_namespace(
            "openSearch", "http://a9.com/-/spec/opensearch/1.1/"
        )

        # Namespace dictionary
        ns = {
            "": "http://www.w3.org/2005/Atom",
            "leg": "http://www.legislation.gov.uk/namespaces/legislation",
            "ukm": "http://www.legislation.gov.uk/namespaces/metadata",
            "theme": "http://www.legislation.gov.uk/namespaces/theme",
            "openSearch": "http://a9.com/-/spec/opensearch/1.1/",
        }

        def _do_request():
            # Get search results and parse XML data (root)
            response = requests.get(
                self.search_url,
                params=params,
                headers=headers,
                timeout=config.timeout,
            )
            if response.status_code == 200:
                root = ET.fromstring(
                    response.content.decode("utf-8")
                )  # nosec BXXX
            else:
                root = None

            try:
                # Extract pagination values
                page_data = {
                    "page": (
                        root.find(".//leg:page", ns).text
                        if root.find(".//leg:page", ns) is not None
                        else None
                    ),
                    "morePages": (
                        root.find(".//leg:morePages", ns).text
                        if root.find(".//leg:morePages", ns) is not None
                        else None
                    ),
                }

                logger.info(f"legislation page data: {page_data}")
                return root, page_data
            except Exception as e:
                logger.error(f"error fetching legislation: {e}")
                return None, None

        root, page_data = _do_request()

        if not root:
            return []

        all_entries = []

        def _extract_entries(root):
            # Extract entries
            entries = []
            for entry in root.findall("entry", ns):
                entry_id = (
                    entry.find("id", ns).text
                    if entry.find("id", ns) is not None
                    else None
                )
                title = (
                    entry.find("title", ns).text
                    if entry.find("title", ns) is not None
                    else None
                )
                updated = (
                    entry.find("updated", ns).text
                    if entry.find("updated", ns) is not None
                    else None
                )
                published = (
                    entry.find("published", ns).text
                    if entry.find("published", ns) is not None
                    else "N/A"
                )  # Placeholder if missing
                summary = (
                    entry.find("summary", ns).text
                    if entry.find("summary", ns) is not None
                    else "N/A"
                )  # Placeholder if missing
                entries.append(
                    {
                        "id": _encode_url(entry_id),
                        "title": title,
                        "date_modified": updated if updated else published,
                        "publisher": "Legislation",
                        "description": summary,
                        "type": "Legislation",
                    }
                )
            return entries

        all_entries += _extract_entries(root)

        morePages = int(page_data["morePages"])
        logger.info(f"legislation more pages: {morePages}")
        if morePages > 1:
            # Get remaining pages
            for page in range(2, morePages + 1):
                root, _ = _do_request()
                all_entries.append(_extract_entries(root))

        logger.info(f"legislation total results: {len(all_entries)}")
        return all_entries
