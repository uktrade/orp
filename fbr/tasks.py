import time

from config.celery import celery_app
from fbr.cache.legislation import Legislation
from fbr.cache.public_gateway import PublicGateway
from fbr.search.config import SearchDocumentConfig
from fbr.search.utils.documents import clear_all_documents


@celery_app.task(name="fbr.tasks.rebuild_cache")
def rebuild_cache() -> None:
    """
    Rebuilds the cache for search documents across various components by
    clearing all existing documents. The process is timed, and the
    duration is included in the success response. If an exception occurs,
    an error message is returned.

    Returns:
        dict: A dictionary containing either a success message with the
        duration of the cache rebuilding process or an error message
        detailing the exception that was raised.
    """
    try:
        start = time.time()
        clear_all_documents()
        config = SearchDocumentConfig(search_query="", timeout=20)
        Legislation().build_cache(config)
        PublicGateway().build_cache(config)
        end = time.time()
        message = {
            "message": "rebuilt cache",
            "duration": round(end - start, 2),
        }
        print(message)
    except Exception as e:
        message = {"message": f"error building cache data: {e}"}
        print(message)
