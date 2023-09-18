from django.db import models

# Create your models here.

class Page(models.Model):
    title = models.CharField(verbose_name="Título", max_length=200)
    content = models.TextField(verbose_name="Contemido")
    order = models.SmallIntegerField(verbose_name="Orden", default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Edición")
    
    class Meta:
        verbose_name = "pagina"#Cambia los nombres en el admina español
        verbose_name_plural = "paginas"
        ordering = ['order', 'title']#Se ordenan los proyectos de los ultimos subidos
        
    def __str__(self):
        return self.title