from django.contrib import admin

from solo.admin import SingletonModelAdmin

from apps.website.models import Website


@admin.register(Website)
class WebsiteAdmin(SingletonModelAdmin):
    fieldsets = (
        (None, {'fields': ('seo_title', 'seo_description')}),
        ('Политика конфиденциальности', {
            'classes': ('collapse', 'open'),
            'fields': ('policy',),
        }),
    )
