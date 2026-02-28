from django.db import models

from filer.fields.image import FilerImageField


class AboutImages(models.Model):
    order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )
    logo = FilerImageField(
        null=False, blank=False,
        on_delete=models.CASCADE,
        related_name='+'
    )

    class Meta:
        ordering = ['order']
