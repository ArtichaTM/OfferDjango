from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_delete

from filer.fields.image import FilerImageField


class AboutImages(models.Model):
    order = models.PositiveIntegerField(
        verbose_name='Порядок',
        default=0,
        blank=False,
        null=False,
    )
    logo = FilerImageField(
        verbose_name='Изображение',
        null=False, blank=False,
        on_delete=models.CASCADE,
        related_name='xz'
    )

    class Meta:
        ordering = ['-order']
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"


@receiver(post_delete, sender=AboutImages)
def mymodel_post_delete(sender, instance: AboutImages, using, **kwargs):
    instance.logo.delete()
