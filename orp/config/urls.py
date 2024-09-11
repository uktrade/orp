"""orp URL configuration."""

import orp_search.views as orp_views

from django.conf import settings
from django.contrib import admin
from django.urls import path

import core.views as core_views

urlpatterns = [
    # path("", core_views.home, name="home"),
    # Uncomment the above line and comment out
    # the two lines below to switch to the app
    # home page.
    path("", core_views.hello_world, name="hello_world"),
    path("home/", core_views.home, name="home"),
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
    path("search/", orp_views.search, name="search"),
]

if settings.DJANGO_ADMIN:
    urlpatterns.append(path("admin/", admin.site.urls))
