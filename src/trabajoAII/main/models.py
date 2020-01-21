from django.db import models


class Album(models.Model):
    albumId = models.AutoField(primary_key=True)
    titulo = models.TextField(verbose_name='Titulo')
    imagen = models.TextField(verbose_name='Imagen')
    precioOriginal = models.TextField(verbose_name='Precio original')
    precioDescuento = models.TextField(verbose_name='Precio con descuento')
    fecha = models.DateField(verbose_name='Fecha de lanzamiento')
    ventas = models.IntegerField(verbose_name='Numero de ventas')
    
    def __str__(self):
        return self.titulo
    
    class Meta:
        ordering = ('titulo', )