from django.contrib import admin
from .models import Habito

# Register your models here.
class HabitoAdmin(admin.ModelAdmin):
    list_display = ('created', 'updated')

    # Inyectamos fichero css
    class Media:
        css = {
            'all': ('habitos/css/custom_ckeditor.css',)
        }

admin.site.register(Habito, HabitoAdmin)