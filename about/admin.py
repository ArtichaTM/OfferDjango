from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin

from . import models

@admin.register(models.AboutImages)
class AboutImagesAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['order', 'logo']
