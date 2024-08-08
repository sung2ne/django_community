from django.contrib import admin
from django.urls import include, path
from common import views as common_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", common_views.main_page, name="main_page"),
    path("admin/", admin.site.urls),
    path("common/", include("common.urls")),
    path("common2/", include("common2.urls")),
    path("board/", include("board.urls")),
]