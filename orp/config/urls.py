"""orp URL configuration."""

import logging
import time

import orp_search.views as orp_search_views

from orp_search.config import SearchDocumentConfig
from orp_search.models import DataResponseModel
from orp_search.utils.documents import clear_all_documents
from orp_search.utils.search import get_publisher_names, search
from rest_framework import routers, serializers, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from django.conf import settings
from django.contrib import admin
from django.urls import include, path

import core.views as core_views

urls_logger = logging.getLogger(__name__)


# Serializers define the API representation.
class DataResponseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DataResponseModel
        fields = [
            "id",
            "title",
            "link",
            "publisher",
            "language",
            "format",
            "description",
            "date_issued",
            "date_modified",
            "date_valid",
            "audience",
            "coverage",
            "subject",
            "type",
            "license",
            "regulatory_topics",
            "status",
            "date_uploaded_to_orp",
            "has_format",
            "is_format_of",
            "has_version",
            "is_version_of",
            "references",
            "is_referenced_by",
            "has_part",
            "is_part_of",
            "is_replaced_by",
            "replaces",
            "related_legislation",
            "id",
        ]


class DataResponseViewSet(viewsets.ModelViewSet):
    @action(detail=False, methods=["get"], url_path="search")
    def search(self, request, *args, **kwargs):
        context = {
            "service_name": settings.SERVICE_NAME_SEARCH,
        }

        try:
            response_data = search(context, request)

            # Create a json object from context but exclude paginator
            response_data = {
                "results": response_data["results"],
                "results_count": response_data["results_count"],
                "is_paginated": response_data["is_paginated"],
                "results_total_count": response_data["results_total_count"],
                "results_page_total": response_data["results_page_total"],
                "current_page": response_data["current_page"],
                "start_index": response_data["start_index"],
                "end_index": response_data["end_index"],
            }

            # Return the response
            return Response(response_data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                data={"message": f"error searching: {e}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class RebuildCacheViewSet(viewsets.ViewSet):
    @action(detail=False, methods=["post"], url_path="rebuild")
    def rebuild_cache(self, request, *args, **kwargs):
        from orp_search.legislation import Legislation
        from orp_search.public_gateway import PublicGateway

        tx_begin = time.time()
        try:
            clear_all_documents()
            config = SearchDocumentConfig(search_query="", timeout=20)
            Legislation().build_cache(config)
            PublicGateway().build_cache(config)
        except Exception as e:
            return Response(
                data={"message": f"[urls] error clearing documents: {e}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        tx_end = time.time()
        urls_logger.info(
            f"time taken to rebuild cache: "
            f"{round(tx_end - tx_begin, 2)} seconds"
        )
        return Response(
            data={
                "message": "rebuilt cache",
                "duration": round(tx_end - tx_begin, 2),
            },
            status=status.HTTP_200_OK,
        )


class PublishersViewSet(viewsets.ViewSet):
    @action(detail=False, methods=["get"], url_path="publishers")
    def publishers(self, request, *args, **kwargs):
        try:
            publishers = get_publisher_names()

            results = [
                {
                    "label": item["trimmed_publisher"],
                    "name": item["trimmed_publisher_id"],
                }
                for item in publishers
            ]

            return Response(
                data={"results": results},
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            return Response(
                data={"message": f"error fetching publishers: {e}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r"v1", DataResponseViewSet, basename="search")
router.register(r"v1/cache", RebuildCacheViewSet, basename="rebuild")
router.register(r"v1/retrieve", PublishersViewSet, basename="publishers")

urlpatterns = [
    path("api/", include(router.urls)),
    path("", orp_search_views.search_react, name="search_react"),
    path("nojs/", orp_search_views.search_django, name="search_django"),
    # If we choose to have a start page with green button, this is it:
    # path("", core_views.home, name="home"),
    path(
        "download_csv/",
        orp_search_views.download_search_csv,
        name="download_csv",
    ),
    path("document/<str:id>", orp_search_views.document, name="document"),
    path("healthcheck/", core_views.health_check, name="healthcheck"),
    path(
        "accessibility-statement/",
        core_views.accessibility_statement,
        name="accessibility-statement",
    ),
    path("privacy-notice/", core_views.privacy_notice, name="privacy-notice"),
    path("cookies/", core_views.cookies, name="cookies"),
    path(
        "set-cookie-banner-preference/",
        core_views.set_cookie_banner_preference,
        name="set-cookie-banner-preference",
    ),
    path(
        "hide-cookie-banner/",
        core_views.hide_cookie_banner,
        name="hide-cookie-banner",
    ),
    # path("search/", orp_views.search, name="search"),
]

if settings.DJANGO_ADMIN:
    urlpatterns.append(path("admin/", admin.site.urls))
