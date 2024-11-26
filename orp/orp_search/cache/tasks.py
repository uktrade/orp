from celery import shared_task
from orp_search.cache.rebuild import rebuild_cache


@shared_task
def rebuild_cache_task():
    return rebuild_cache()
