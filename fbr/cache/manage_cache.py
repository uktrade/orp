# flake8: noqa
import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
django.setup()


import time

from fbr.cache.legislation import Legislation
from fbr.cache.public_gateway import PublicGateway
from fbr.search.config import SearchDocumentConfig
from fbr.search.utils.documents import clear_all_documents


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
