from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('api/', include('project.api_urls', namespace='api')),
    path('', include('apps.website.urls', namespace='website')),
] + static(prefix=settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += [
        path('documentation/', TemplateView.as_view(template_name='swagger/swagger.html'), name='documentation'),
    ]
