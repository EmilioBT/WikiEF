from django import forms 
from .models import Page

class PageForm(forms.ModelForm):
    
    class Meta:

        model = Page
        fields = ['title', 'content','link', 'order' ]
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Título'}),
            'content':forms.Textarea(attrs={'class':'form-control'}),
            'link': forms.URLInput(attrs={'class':'form-control', 'placeholder':'Url'}),
            'order':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Orden'})
        }

        labels = {
            'title':'', 'content':'', 'link':'', 'order':''
        }