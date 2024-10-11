import logging

logger = logging.getLogger(__name__)


class SearchDocumentConfig:
    def __init__(
        self, search_terms: str, document_types=None, timeout=None, dummy=False
    ):
        """
        Initializes a new instance of the class.

        :param searchTerms: A comma-separated string of search terms.
        :param documentTypes: Optional. A list of document types
                              to filter the search.
        :param timeout: Optional. The timeout in seconds for the search
                        request.
        """
        self.search_terms = [term.strip() for term in search_terms.split(",")]
        self.document_types = document_types
        self.timeout = None if timeout is None else int(timeout)
        self.dummy = dummy

    def validate(self):
        """

        Validates the presence of search terms.

        Checks if the 'searchTerms' attribute exists and is non-empty. Logs
        an error message and returns False if 'searchTerms' is missing or
        empty.

        Returns
        -------
        bool
            True if 'searchTerms' is present and non-empty, False otherwise.
        """
        if not self.search_terms:
            logger.error("search terms are required")
            return False
        return True
