from django.db import models


class Link(models.Model):
    key = models.SlugField(max_length=100, unique=True, verbose_name="Slug")
    name = models.CharField(max_length=100, verbose_name="Red Social")
    url = models.URLField(max_length=200, null=True, blank=True, verbose_name="URL")
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Actualizacion')

    class Meta:
        verbose_name = 'enlace'
        verbose_name_plural = 'enlaces'
        ordering = ['name']

    def __str__(self):
        return self.name
