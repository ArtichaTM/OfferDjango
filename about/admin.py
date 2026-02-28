from django.contrib import admin
from django.utils.html import format_html

from adminsortable2.admin import SortableAdminMixin

from . import models


@admin.register(models.AboutImages)
class AboutImagesAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['logo_preview', 'custom_logo_display', 'order']
    list_display_links = ['logo_preview']

    def logo_preview(self, obj):
        return format_html('<img src="{}" />', obj.logo.thumbnails['admin_clipboard_icon'])

    
    def custom_logo_display(self, obj):
        return obj.logo.label

    logo_preview.short_description = "Предпросмотр"
    custom_logo_display.admin_order_field = 'logo'
    custom_logo_display.short_description = 'Название'
