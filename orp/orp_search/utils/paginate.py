from orp_search.config import SearchDocumentConfig

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def paginate(context, config: SearchDocumentConfig, search_results):
    paginator = Paginator(search_results, config.limit)
    try:
        paginated_documents = paginator.page(config.offset)
    except PageNotAnInteger:
        paginated_documents = paginator.page(1)
    except EmptyPage:
        paginated_documents = paginator.page(paginator.num_pages)

    # Iterate over each document in paginated_documents
    if paginated_documents:
        for paginated_document in paginated_documents:
            if "description" in paginated_document:
                description = paginated_document["description"]

                # If description is not an empty string
                if description:
                    # Truncate description to 100 characters
                    paginated_document["description"] = (
                        description[:100] + "..."
                        if len(description) > 100
                        else description
                    )
            if "regulatory_topics" in paginated_document:
                paginated_document["regulatory_topics"] = str(
                    paginated_document["regulatory_topics"]
                ).split("\n")

    context["paginator"] = paginator
    context["results"] = paginated_documents
    context["results_count"] = len(paginated_documents)
    context["is_paginated"] = paginator.num_pages > 1
    context["results_total_count"] = paginator.count
    context["results_page_total"] = paginator.num_pages
    context["current_page"] = config.offset
    context["start_index"] = paginated_documents.start_index()
    context["end_index"] = paginated_documents.end_index()

    return context
