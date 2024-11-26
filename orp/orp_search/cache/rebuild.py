import logging
import time

from orp_search.cache.legislation import Legislation
from orp_search.cache.public_gateway import PublicGateway
from orp_search.config import SearchDocumentConfig
from orp_search.utils.documents import clear_all_documents
from rest_framework import status

logger = logging.getLogger(__name__)


def rebuild_cache():
    """
    Rebuilds cache for Legislation and PublicGateway.

    This function clears all existing documents and rebuilds the cache
    using specified configurations. If an error occurs during the process,
    an error message is returned with HTTP status 500. Otherwise, a success
    message along with the duration time taken to rebuild the cache is returned
    with HTTP status 200.

    Returns:
        dict: Response dictionary containing the status and message.
    """
    tx_begin = time.time()
    try:
        clear_all_documents()
        config = SearchDocumentConfig(search_query="", timeout=20)
        Legislation().build_cache(config)
        PublicGateway().build_cache(config)
    except Exception as e:
        return {
            "data": {"message": f"[urls] error clearing documents: {e}"},
            "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
        }

    tx_end = time.time()

    logger.debug(
        f"time taken to rebuild cache: "
        f"{round(tx_end - tx_begin, 2)} seconds"
    )

    return {
        "data": {
            "message": "rebuilt cache",
            "duration": round(tx_end - tx_begin, 2),
        },
        "status": status.HTTP_200_OK,
    }
