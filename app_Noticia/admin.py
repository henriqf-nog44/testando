from django.contrib import admin
from .models import Noticia, Tag, Pessoa

@admin.register(Noticia, Tag, Pessoa)
class NoticiaAdmin(admin.ModelAdmin):
    pass
# Register your models here.
