import time

from celery import shared_task

from fbr.cache.legislation import Legislation
from fbr.cache.public_gateway import PublicGateway
from fbr.search.config import SearchDocumentConfig
from fbr.search.utils.documents import clear_all_documents


@shared_task(binding=True)
def rebuild_cache():
    try:
        start = time.time()
        clear_all_documents()
        config = SearchDocumentConfig(search_query="", timeout=20)
        Legislation().build_cache(config)
        PublicGateway().build_cache(config)
        end = time.time()
        return {"message": "rebuilt cache", "duration": round(end - start, 2)}
    except Exception as e:
        return {"message": f"error clearing documents: {e}"}
