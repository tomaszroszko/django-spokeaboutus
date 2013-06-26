from django.contrib import admin
from django.template.defaultfilters import truncatewords
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _

from .models import SpokeAboutUs, SpokeSource


def get_messages(modeladmin, request, queryset):
    """
        Collect messages from selected sources
    """
    for source in queryset:
        sc = source.source_class(spoke_source=source)
        sc.collect_messages()
        source.updated = now()
        source.save()
get_messages.short_description = _('Get Messages from selected sources')


class SpokeSourceAdmin(admin.ModelAdmin):
    list_display = ('spoke_source', 'search_query', 'updated', 'is_active')
    list_filter = ('spoke_source', 'search_query', 'updated', 'is_active')
    list_edtiable = ('is_active', 'search_query')
    actions = [get_messages]

class SpokeAboutUsAdmin(admin.ModelAdmin):
    list_display = ('spoke_source', 'author', 'about_us_admin', 'spoke_date',
                    'is_active', 'order')
    list_filter = ('is_active', 'spoke_source')
    list_editable = ('is_active', 'order', 'author', 'spoke_date')

    def about_us_admin(self, obj):
        return truncatewords(obj.about_us, 20)
    about_us_admin.short_description = _('About Us')


admin.site.register(SpokeAboutUs, SpokeAboutUsAdmin)
admin.site.register(SpokeSource, SpokeSourceAdmin)