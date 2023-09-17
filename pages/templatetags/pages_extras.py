from django import template
from pages.models import Page


# Creamos un metodo
register = template.Library()

# Pasamos la funcion a Tag, que se guarda en la libreria
@register.simple_tag

# Funsion del tag
def get_pages_list():
    pages = Page.objects.all()
    return pages