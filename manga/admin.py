from django.contrib import admin
from .models import Manga,Genero
# Register your models here.

@admin.register(Manga)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ["titulo","autor","precio","genero"] 
    list_filter = ["precio","stock_copias","genero"]
    search_fields = ["fecha_publicacion"]

@admin.register(Genero)
class GeneroaAdmin(admin.ModelAdmin):
    list_display = ["nombre","descripcion"] 
    list_filter = ["nombre","descripcion"]
    search_fields = ["nombre","descripcion"]
