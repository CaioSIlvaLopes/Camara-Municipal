
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from docs.views import docs_view, docs_vizualizer# pega a pasta doc e importa a funçao para a viewer


urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/',docs_view, name='docs_list'),
    path('docs/<int:doc_id>/', docs_vizualizer, name='docs_vizualizer'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
