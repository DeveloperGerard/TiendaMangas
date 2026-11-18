from django.db import models

# Create your models here.

class Genero(models.Model):
    nombre = models.CharField(max_length=30,verbose_name="Nombre")
    descripcion = models.TextField(blank=True,null=True)
    def __str__(self):
        return self.nombre



class Manga(models.Model):
    isbn = models.CharField(max_length=20, unique=True, verbose_name="ISBN")
    titulo = models.CharField(max_length=150, verbose_name='Título del Libro')
    autor = models.CharField(max_length=100, verbose_name='Autor')
    precio = models.IntegerField(verbose_name='Precio ($ CLP)')
    stock_copias = models.IntegerField(verbose_name='Copias Disponibles')
    disponible = models.BooleanField(default=True, verbose_name='Disponible')
    fecha_publicacion = models.DateField(verbose_name='Fecha de Publicación', null=True)
    
    #LLAVE FORANEA
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE, null=True, blank=True, related_name='mangas')

    def __str__(self):
        return f"{self.titulo} ({self.autor})"