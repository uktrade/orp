import logging

from orp_search.utils.terms import parse_search_terms

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
        self.search_terms = [term.strip() for term in search_terms.split(",")]
        self.document_types = document_types
        self.timeout = None if timeout is None else int(timeout)
        self.dummy = dummy
        self.limit = limit
        self.offset = offset
        self.publisher_terms = publisher_terms
        self.sort_by = sort_by
        self.id = id

        # Parse search terms
        search_terms_and, search_terms_or = parse_search_terms(search_terms)
        self.search_terms_and = search_terms_and
        self.search_terms_or = search_terms_or

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

    def build_search_term(self):
        # Rules config.search_terms
        # 1. If search terms is empty, return empty string
        # 2. If search terms begin with a quote and end with a quote
        # then treat as a phrase
        # 3. If search terms contain a + between two terms then treat
        # as an AND search
        # 4. If search terms contain a space between two terms then treat
        # as a OR search

        search_term_tmp = []

        for term in self.search_terms:
            if term.startswith('"') and term.endswith('"'):
                search_term_tmp.append(f'"{term}"')
            elif "+" in term:
                search_term_tmp.append(term.replace("+", " AND "))
            else:
                search_term_tmp.append(term)
