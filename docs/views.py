from django.shortcuts import render, get_object_or_404, redirect
from docs.models import Docs
from django.db.models import Q
from django.core.paginator import Paginator
from docs.forms import DocModelForm


def docs_view(request):
    # Recupera todos os documentos ordenados por tipo
    docs_list = Docs.objects.all().order_by('tipe')

    # Recupera os parâmetros de busca
    search = request.GET.get('search', '')
    tipos = request.GET.get('tipos', '')

    # Filtragem condicional
    if search and tipos:
        docs_list = docs_list.filter(
            Q(autor__icontains=search) & Q(tipe__name__icontains=tipos)
        )
    elif search:
        docs_list = docs_list.filter(autor__icontains=search)
    elif tipos:
        docs_list = docs_list.filter(tipe__name__icontains=tipos)

    # Configuração da paginação
    paginator = Paginator(docs_list, 5)  # Exibe 10 itens por página
    page_number = request.GET.get('page')  # Recupera o número da página atual
    page_obj = paginator.get_page(page_number)  # Obtém os itens da página atual

    return render(
        request,
        'docs.html',
        {'page_obj': page_obj, 'search': search, 'tipos': tipos},
    )


def docs_vizualizer(request, doc_id):
#     Recupera o documento pelo ID ou retorna erro 404
    doc = get_object_or_404(Docs, id=doc_id)

 #   Renderiza o template com o documento
    return render(request, 'vizualizer.html', {'doc': doc})



def new_doc_view(request):
    if request.method =='POST':
        new_doc_form = DocModelForm(request.POST, request.FILES)
        if new_doc_form.is_valid():
            new_doc_form.save()
            return redirect('docs_list')

    else:
     new_doc_form = DocModelForm()
    return render(request, 'new_doc.html',{'new_doc_form': new_doc_form})

# #teste
# def print_image_view(request, image_id):
#     image_url = f'/media/{image_id}.jpg'  # Exemplo de caminho da imagem
#     return render(request, 'vizualizer.html', {'image_url': image_url})