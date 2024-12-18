from django.db import models

# Create your models here.

class Proyecto (models.Model):
    title = models.CharField(max_length=200, verbose_name = "Título", null=True, blank=True)
    image = models.ImageField(verbose_name = "Imagen", upload_to="proyecto", null=True, blank=True)
    link = models.URLField(verbose_name="Dirección Web", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name = "Fecha creación")
    updated = models.DateTimeField(auto_now=True, verbose_name = "Fecha actualización")

    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["created"]

    def __str__(self):
        return self.title