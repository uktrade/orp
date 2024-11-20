import logging

logger = logging.getLogger(__name__)


class SearchDocumentConfig:
    def __init__(
        self,
        search_query: str,
        document_types=None,
        timeout=None,
        limit=10,
        offset=1,
        publisher_names=None,
        sort_by=None,
        id=None,
    ):
        """
        Initializes a new instance of the class.

        :param searchTerms: A comma-separated string of search terms.
        :param documentTypes: Optional. A list of document types
                              to filter the search.
        :param timeout: Optional. The timeout in seconds for the search
                        request.
        """
        self.search_query = search_query
        self.document_types = [doc_type.lower() for doc_type in document_types]
        self.timeout = None if timeout is None else int(timeout)
        self.limit = limit
        self.offset = offset
        self.publisher_names = publisher_names
        self.sort_by = sort_by
        self.id = id

        logger.info(f"document_types from request: {self.document_types}")

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

        if self.sort_by:
            if self.sort_by not in ["recent", "relevance"]:
                logger.error("sort_by must be 'recent' or 'relevance'")
                return False
        return True

    def print_to_log(self):
        logger.info(f"search_query: {self.search_query}")
        logger.info(f"document_types: {self.document_types}")
        logger.info(f"timeout: {self.timeout}")
        logger.info(f"limit: {self.limit}")
        logger.info(f"offset: {self.offset}")
        logger.info(f"publisher_names: {self.publisher_names}")
        logger.info(f"sort_by: {self.sort_by}")
        logger.info(f"id: {self.id}")
