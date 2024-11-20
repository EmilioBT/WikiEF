from django.contrib import admin
from .models import Ejercicio

# Register your models here.
class EjercicioAdmin(admin.ModelAdmin):
        readonly_fields = ('created', 'updated')

        # Inyectamos fichero css
        class Media:
                css = {
                'all': ('ejercicios/css/custom_ckeditor.css',)
                }

admin.site.register(Ejercicio, EjercicioAdmin)