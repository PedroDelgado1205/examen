from django.db import models

# Create your models here.

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    fecha_publicacion = models.DateField()
    isbn = models.CharField(max_length=13)
    ruta_img = models.ImageField(upload_to='imagenes/', verbose_name="Imagen", null=True)

    def __str__(self):
        return self.titulo