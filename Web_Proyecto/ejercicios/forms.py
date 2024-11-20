from django import forms 
from .models import Ejercicio

class EjercicioForm(forms.ModelForm):
    
    class Meta:

        model = Ejercicio
        fields = ['title', 'image', 'description','link' ]
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Título'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control', 'placeholder': 'Imagen'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
            'link': forms.URLInput(attrs={'class':'form-control', 'placeholder':'Url'}),
        }

        labels = {
            'title':'', 'image':'', 'description':'', 'link':''
        }