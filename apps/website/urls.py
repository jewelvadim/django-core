from django.urls import path

from apps.website.views import IndexTemplateView


app_name = 'website'

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
]
