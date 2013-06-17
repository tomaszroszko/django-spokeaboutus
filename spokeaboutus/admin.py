from django.contrib import admin
from django.template.defaultfilters import truncatewords
from django.utils.translation import ugettext_lazy as _

from .models import SpokeAboutUs, SpokeSource


class SpokeSourceAdmin(admin.ModelAdmin):
    list_display = ('spoke_source', 'search_query', 'updated', 'is_active')
    list_filter = ('spoke_source', 'search_query', 'updated', 'is_active')
    list_edtiable = ('is_active', 'search_query')


class SpokeAboutUsAdmin(admin.ModelAdmin):
    list_display = ('author', 'about_us_admin', 'spoke_source', 'spoke_date',
                    'is_active', 'order')
    list_filter = ('is_active', 'spoke_source')
    list_editable = ('is_active', 'order')

    def about_us_admin(self, obj):
        return truncatewords(obj.about_us, 20)
    about_us_admin.short_description = _('About Us')


admin.site.register(SpokeAboutUs, SpokeAboutUsAdmin)
admin.site.register(SpokeSource, SpokeSourceAdmin)