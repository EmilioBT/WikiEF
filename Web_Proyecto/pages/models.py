from django.db import models
from ckeditor.fields import RichTextField

class Page(models.Model):
    title = models.CharField(max_length=200, verbose_name = "Título")
    subtitle  = models.CharField(max_length=200, verbose_name = "subtítulo", null=True, blank=True)
    content = RichTextField(verbose_name="Contenido")
    link = models.URLField(verbose_name="Dirección Web", null=True, blank=True)  
    order = models.SmallIntegerField(verbose_name="Orden", default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "página"
        verbose_name_plural = "pages"
        ordering = ['order', 'title']

    def __str__(self):
        return self.title
