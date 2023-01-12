from django.conf import settings

from rest_framework.routers import BaseRouter, DefaultRouter, SimpleRouter


def get_drf_router() -> BaseRouter:
    return DefaultRouter() if settings.DEBUG else SimpleRouter()
