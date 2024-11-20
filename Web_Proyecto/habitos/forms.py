from django import forms 
from .models import Habito

class HabitoForm(forms.ModelForm):
    
    class Meta:

        model = Habito
        fields = ['title', 'description','link' ]
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Título'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
            'link': forms.URLInput(attrs={'class':'form-control', 'placeholder':'Url'}),
        }

        labels = {
            'title':'', 'description':'', 'link':''
        }