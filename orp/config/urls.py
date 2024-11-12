"""orp URL configuration."""

import orp_search.views as orp_search_views

from orp_search.models import DataResponseModel
from orp_search.utils.documents import clear_all_documents
from orp_search.utils.search import search
from rest_framework import routers, serializers, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from django.conf import settings
from django.contrib import admin
from django.urls import include, path

import core.views as core_views


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
    serializer_class = DataResponseSerializer

    def list(self, request, *args, **kwargs):
        # Assuming `search` is a function that
        # processes the request and returns data
        context = {
            "service_name": settings.SERVICE_NAME_SEARCH,
        }
        response_data = search(context, request)

        # Return the response
        return Response(response_data, status=status.HTTP_200_OK)


class RebuildCacheViewSet(viewsets.ViewSet):
    @action(detail=False, methods=["post"], url_path="cache")
    def rebuild_cache(self, request, *args, **kwargs):
        from orp_search.legislation import Legislation

        # from orp_search.public_gateway import PublicGateway

        try:
            clear_all_documents()
            Legislation().build_cache()
            # PublicGateway().build_cache()
        except Exception as e:
            return Response(
                data={"message": f"error clearing documents: {e}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        return Response(
            data={"message": "rebuilt cache"}, status=status.HTTP_200_OK
        )


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r"dataresults", DataResponseViewSet, basename="dataresponse")
router.register(r"rebuild", RebuildCacheViewSet, basename="cache")

urlpatterns = [
    path("", include(router.urls)),
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
