from django.contrib import admin
from django.urls import include, path
from common import views as common_views
from django.conf import settings
from django.conf.urls.static import static

def trigger_error(request):
    division_by_zero = 1 / 0
    
urlpatterns = [
    path('sentry-debug/', trigger_error),
    path("", common_views.main_page, name="main_page"),
    path('summernote/', include('django_summernote.urls')),
    path("admin/", admin.site.urls),
    path("common/", include("common.urls")),
    path("common2/", include("common2.urls")),
    path("board/", include("board.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
