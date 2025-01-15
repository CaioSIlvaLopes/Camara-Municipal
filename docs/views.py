from django.shortcuts import render

from docs.models import Docs 



def docs_view(request):

     docs = Docs.objects.all()# pega todos os objetos do banco de dados all
     
     search = request.GET.get('search')

     if search:
          docs = Docs.object.filter(tipe__icontains =search)
     
     return render(
          request ,
         'docs.html', 
         {'docs': docs})#pega o arquivo HTML da pasta templates ejoga para o usuario 
 