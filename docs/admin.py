from django.contrib import admin
from docs.models import Docs,Type


class DocAdmin(admin.ModelAdmin):
    list_display = ('id','tipe', 'autor','date')
    
    search_fields = ('tipe','autor')


admin.site.register(Docs, DocAdmin)

class TypeAdmin(admin.ModelAdmin):
    list_display=('name',)
    search_fields = ('name',)#buscando o tipo de doc

admin.site.register(Type,TypeAdmin)