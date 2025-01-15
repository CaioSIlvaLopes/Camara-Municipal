from django.shortcuts import render
from docs.models import Docs 
from django.db.models import Q



def docs_view(request):
     docs =Docs.objects.all().order_by('tipe')
     search = request.GET.get('search')
     tipos = request.GET.get('tipos')
     

     if not tipos:
          docs = Docs.objects.filter(Q(autor__icontains=search)|Q(tipe__name__icontains=tipos))
     
     if search and tipos:
      docs = Docs.objects.filter(autor__icontains = search, tipe__name__icontains = tipos)
     

     return render(
          request ,
         'docs.html', 
         {'docs': docs})#pega o arquivo HTML da pasta templates e joga para o usuario 
 