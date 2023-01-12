from django.urls import path
from django.views.decorators.csrf import ensure_csrf_cookie

from apps.website.views import IndexTemplateView


app_name = 'website'

urlpatterns = [
    path('', ensure_csrf_cookie(IndexTemplateView.as_view()), name='index'),
]
