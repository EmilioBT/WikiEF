from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Ejercicio(models.Model):
    title = models.CharField(max_length=200, verbose_name = "Título")
    image = models.ImageField(verbose_name = "Imagen", upload_to="ejercicio", null=True, blank=True)
    description = RichTextField(verbose_name = "Descripción")
    link = models.URLField(verbose_name="Dirección Web", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name = "Fecha creación")
    updated = models.DateTimeField(auto_now=True, verbose_name = "Fecha actualización")
    
    class Meta:
        verbose_name = "ejercicio"
        verbose_name_plural = "ejercicios"
        ordering = ["created"]

    def __str__(self):
        return self.title