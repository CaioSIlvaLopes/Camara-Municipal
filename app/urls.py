
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from docs.views import docs_vizualizer

from docs.views import docs_view# pega a pasta doc e importa a funçao para a viewer


urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/',docs_view, name='docs_list'),
    path('vizualizer/', docs_vizualizer, name='vizualizer'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
