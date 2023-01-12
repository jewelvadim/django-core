from typing import Any, Unpack

from django.conf import settings
from django.views.generic import TemplateView

from apps.core.decorators import query_debugger
from apps.website.models import Website


class IndexTemplateView(TemplateView):
    template_name = 'index.html'

    @query_debugger
    def get_context_data(self, **kwargs: Unpack) -> dict[str, Any]:
        print(kwargs, type(kwargs))

        context = super().get_context_data(**kwargs)

        website = Website.get_solo()

        context['debug'] = settings.DEBUG
        context['seo_title'] = website.seo_title
        context['seo_description'] = website.seo_description

        return context
