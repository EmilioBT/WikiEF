from django import forms 
from .models import Herramienta

class HerramientaForm(forms.ModelForm):
    
    class Meta:

        model = Herramienta
        fields = ['title', 'description','link' ]
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Título'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
            'link': forms.URLInput(attrs={'class':'form-control', 'placeholder':'Url'}),
        }

        labels = {
            'title':'', 'description':'', 'link':''
        }