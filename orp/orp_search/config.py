import logging

logger = logging.getLogger(__name__)


class SearchDocumentConfig:
    def __init__(
        self,
        search_terms: str,
        document_types=None,
        timeout=None,
        dummy=False,
        limit=10,
        offset=1,
        publisher_terms=None,
        sort_by=None,
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
        self.limit = limit
        self.offset = offset
        self.publisher_terms = publisher_terms
        self.sort_by = sort_by

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
        if self.offset < 0:
            logger.error("offset must be a positive integer")
            return False

        if self.limit < 0:
            logger.error("limit must be a positive integer")
            return False
        return True
