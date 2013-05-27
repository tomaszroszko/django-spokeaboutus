from django.contrib import admin
from .models import SpokeSource, SpokeAboutUs


class SpokeSourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')
    list_filter = ('is_active',)
    list_editable = ('is_active',)


class SpokeAboutUsAdmin(admin.ModelAdmin):
    list_display = ('author', 'about_us', 'spoke_source', 'spoke_date',
                    'is_active', 'order')
    list_filter = ('is_active', 'spoke_source')
    list_editable = ('is_active', 'order')


admin.site.register(SpokeSource, SpokeSourceAdmin)
admin.site.register(SpokeAboutUs, SpokeAboutUsAdmin)
