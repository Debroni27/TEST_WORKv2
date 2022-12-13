import uuid

from django.db import models
from django_resized import ResizedImageField


class BaseModel(models.Model):
    """Basic Model"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created_at', '-updated_at']


class BaseImage(models.Model):
    """Basic model for images"""
    path = ResizedImageField('Изображение', quality=75, force_format="WEBP", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return 'Изображение'