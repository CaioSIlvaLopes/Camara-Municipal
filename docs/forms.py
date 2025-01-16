from django import forms
from docs.models import  Docs


class DocModelForm(forms.ModelForm):
        
        class Meta:
            model = Docs
            fields = '__all__'


# def clean_tipe(self): validaçoes 
#       tipe = self.cleaned_data.get('tipe')
#       if 

#       self.add_error()