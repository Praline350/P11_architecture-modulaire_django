from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from . import views


def trigger_error(request):
    return 1 / 0


urlpatterns = [
    path("sentry-debug/", trigger_error),
    path("log/", views.test_log_view),
    path("", views.index, name="index"),
    path("lettings/", include("lettings.urls")),
    path("profiles/", include("profiles.urls")),
    path("admin/", admin.site.urls),
]

handler404 = "oc_lettings_site.views.handler404"
handler500 = "oc_lettings_site.views.handler500"


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
