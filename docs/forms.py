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
 

 #testando 
# class SeuModeloForm(forms.ModelForm):
#     class Meta:
#         model = Docs
#         fields = '__all__'  # Ou liste os campos específicos que deseja incluir
#         labels = {
#             'tipe': 'Tipo do Documento',
#             'autor': 'Nome do Autor',
        # }