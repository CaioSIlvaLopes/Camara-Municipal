from django.db import models

class Type(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)


    def __str__(self):
      return self.name



class Docs(models.Model):#tabela documentos
    id = models.AutoField(primary_key=True)
    tipe = models.ForeignKey(Type, on_delete=models.PROTECT, related_name='type_doc')
    autor = models.CharField(max_length=200)
    year = models.IntegerField(blank=True, null=True)
    photo = models.ImageField(upload_to='docs/', blank=True, null=True)
    

    def __str__(self): 
        return self.autor#retorna na tabela o nome do autor