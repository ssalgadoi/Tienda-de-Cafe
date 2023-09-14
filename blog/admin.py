from django.contrib import admin
from .models import Category, Post
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title','author', 'published')# Esto me mostraras estas tres columnas
    ordering = ('author', 'published')# Ordena por 
    
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)

# En resumen, este código personaliza cómo se muestran los modelos 
# Category y Post en el panel de administración de Django al hacer que 
# los campos de fecha de creación y fecha de edición sean de solo lectura 
# y los registra para que puedas administrarlos fácilmente en el panel de administración.
# esto tambien hace que se visualice en el panel de admin