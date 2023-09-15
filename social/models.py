from django.db import models

# Create your models here.

class Link(models.Model):
    key = models.SlugField(verbose_name="Nombre Clave", max_length=100, unique=True)#Solo resibe caracteres especiales
    name = models.CharField(verbose_name="Red social", max_length=100)
    url = models.URLField(verbose_name="Enlace",max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Edición")
    
    class Meta:
        verbose_name = "enlace"#Cambia los nombres en el admina español
        verbose_name_plural = "enlaces"
        ordering = ["-created"]#Se ordenan los proyectos de los ultimos subidos
        
    def __str__(self):
        return self.name