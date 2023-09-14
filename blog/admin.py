from django.contrib import admin
from .models import Category, Post
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title','author', 'published', 'post_categories')# Esto me mostraras estas tres columnas
    ordering = ('author', 'published')# Ordena por author y fecha
    search_fields = ('title', 'content', 'author__username', 'categories__name')# Buscador de contendio en el admin
    #author__username es para buscar por author
    #con el name podemos buscar por categorias
    date_hierarchy = 'published'# Para buscar por gerarquias de fechas, por dias, años
    list_filter = ('author__username', 'categories__name')#Este nos agrega un filtro para poder buscar 
    
    
    # este código personaliza cómo se muestra la información de las categorías en el panel de          #
    # administración de Django para los registros del modelo Post, toma las categorías asociadas a     #
    # un registro y las muestra como una lista separada por comas en una columna llamada "Categorias". #
    def post_categories(self, obj):                                                                    #
        return ",".join([c.name for c in obj.categories.all().order_by("name")])                       # 
    post_categories.short_description = "Categorias"                                                   #
   #####################################################################################################
    
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)

# En resumen, este código personaliza cómo se muestran los modelos 
# Category y Post en el panel de administración de Django al hacer que 
# los campos de fecha de creación y fecha de edición sean de solo lectura 
# y los registra para que puedas administrarlos fácilmente en el panel de administración.
# esto tambien hace que se visualice en el panel de admin