import logging
import time

from orp_search.config import SearchDocumentConfig

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import QuerySet

logger = logging.getLogger(__name__)


def paginate(
    context: dict, config: SearchDocumentConfig, results: QuerySet
) -> dict:
    start_time = time.time()

    logger.info("paginating documents...")
    paginator = Paginator(results, config.limit)
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

    # Convert paginated_documents into a list of json objects
    paginated_documents_json = []
    for paginated_document in paginated_documents:
        paginated_documents_json.append(
            {
                "id": paginated_document.id,
                "title": paginated_document.title,
                "publisher": paginated_document.publisher,
                "description": paginated_document.description,
                "type": paginated_document.type,
                "date_modified": paginated_document.date_modified,
            }
        )

    start_time = time.time()
    context["paginator"] = paginator
    context["results"] = paginated_documents_json
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
