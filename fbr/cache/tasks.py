from celery import shared_task

from fbr.cache.legislation import Legislation
from fbr.cache.public_gateway import PublicGateway
from fbr.search.config import SearchDocumentConfig
from fbr.search.utils.documents import clear_all_documents


@shared_task()
def rebuild_cache():
    try:
        clear_all_documents()
        config = SearchDocumentConfig(search_query="", timeout=20)
        Legislation().build_cache(config)
        PublicGateway().build_cache(config)
        return {"message": "rebuilt cache"}
    except Exception as e:
        return {"message": f"error clearing documents: {e}"}
