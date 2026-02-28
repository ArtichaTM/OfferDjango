from django.contrib import admin
from django.utils.html import format_html

from adminsortable2.admin import SortableAdminMixin

from . import models


@admin.register(models.AboutImages)
class AboutImagesAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['logo_preview', 'logo', 'order']

    def logo_preview(self, obj):
        return format_html('<img src="{}" />', obj.logo.thumbnails['admin_clipboard_icon'])
    logo_preview.short_description = "Предпросмотр"
