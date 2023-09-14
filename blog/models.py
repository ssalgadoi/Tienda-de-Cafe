from django.db import models
from django.utils.timezone import now 
from django.contrib.auth.models import User
# Create your models here.


# Esto se parece a una lista de categorías para los artículos. Cada categoría tiene un nombre como 
# "Deportes", "Ciencia" o "Tecnología". También lleva un registro de cuándo se creó y cuándo se 
# actualizó por última vez. Esto ayuda a organizar las categorías y mostrarlas en el sitio web. 
# Por ejemplo, cuando alguien hace clic en "Deportes", solo verá los artículos relacionados con deportes.

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Edición")
    
    class Meta:
        verbose_name = "categoria"#Cambia los nombres en el admina español
        verbose_name_plural = "categorias"
        ordering = ["-created"]#Se ordenan los proyectos de los ultimos subidos
        
    def __str__(self):
        return self.name
    

# Esta parte es como una hoja en blanco donde puedes escribir artículos. Cada artículo tiene un título, 
# un contenido (el texto del artículo), una fecha de publicación y puede tener una imagen. Además, cada 
# artículo debe tener un autor, que es la persona que lo escribió. Luego, el artículo puede estar en 
# una o más categorías. Por ejemplo, si es un artículo sobre "Fútbol" y "Deportes", pertenecerá a ambas 
# categorías.

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    content = models.TextField(verbose_name="Contenido")
    published = models.DateTimeField(verbose_name="Fecha de publicacion", default=now)
    image = models.ImageField(verbose_name="Imagen", upload_to="blog", null=True, blank=True)
    author = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name="Categorías")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Edición")
    
    class Meta:
        verbose_name = "entrada"#Cambia los nombres en el admina español
        verbose_name_plural = "entradas"
        ordering = ["-created"]#Se ordenan los proyectos de los ultimos subidos
        
    def __str__(self):
        return self.title
    
# Así que, en resumen, estas dos partes de código ayudan a crear y organizar 
# artículos en un sitio web, ¡como si estuvieras escribiendo historias y 
# guardándolas en carpetas para que las personas puedan leerlas fácilmente!
