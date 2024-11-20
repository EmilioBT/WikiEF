from django.contrib import admin
from .models import Herramienta

# Register your models here.
class HerramientaAdmin(admin.ModelAdmin):
        readonly_fields = ('created', 'updated')

        # Inyectamos fichero css
        class Media:
                css = {
                        'all': ('habitos/css/custom_ckeditor.css',)
                }
        
admin.site.register(Herramienta, HerramientaAdmin)