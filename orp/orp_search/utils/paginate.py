import logging
import time

from orp_search.config import SearchDocumentConfig
from orp_search.models import DataResponseModel

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

logger = logging.getLogger(__name__)


def paginate(context: dict, config: SearchDocumentConfig) -> dict:
    start_time = time.time()

    logger.info("paginating documents...")
    documents = DataResponseModel.objects.all().order_by("id")
    paginator = Paginator(documents, config.limit)
    try:
        paginated_documents = paginator.page(config.offset)
    except PageNotAnInteger:
        paginated_documents = paginator.page(1)
    except EmptyPage:
        paginated_documents = paginator.page(paginator.num_pages)

    end_time = time.time()
    logger.info(
        f"time taken to paginate (before description +/ regulatory topics):"
        f" {round(end_time - start_time, 2)} seconds"
    )

    # Iterate over each document in paginated_documents
    if paginated_documents:
        start_time = time.time()

        for paginated_document in paginated_documents:
            if hasattr(paginated_document, "description"):
                description = paginated_document.description
                if description:
                    paginated_document.description = (
                        (
                            description[:100] + "..."
                            if len(description) > 100
                            else description
                        )
                        .lstrip(".")
                        .capitalize()
                    )
            if hasattr(paginated_document, "regulatory_topics"):
                regulatory_topics = paginated_document.regulatory_topics
                if regulatory_topics:
                    paginated_document.regulatory_topics = str(
                        regulatory_topics
                    ).split("\n")

        end_time = time.time()
        logger.info(
            f"time taken to paginate "
            f"(after description +/ regulatory topics): "
            f"{round(end_time - start_time, 2)} seconds"
        )

    start_time = time.time()
    context["paginator"] = paginator
    context["results"] = paginated_documents
    context["results_count"] = len(paginated_documents)
    context["is_paginated"] = paginator.num_pages > 1
    context["results_total_count"] = paginator.count
    context["results_page_total"] = paginator.num_pages
    context["current_page"] = config.offset
    context["start_index"] = paginated_documents.start_index()
    context["end_index"] = paginated_documents.end_index()
    end_time = time.time()
    logger.info(
        f"time taken to paginate (after adding to context): "
        f"{round(end_time - start_time, 2)} seconds"
    )
    return context
