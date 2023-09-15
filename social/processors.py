

# En resumen, este código crea un diccionario que mapea nombres clave de enlaces a sus 
# respectivos URLs. Puede ser útil para proporcionar enlaces en una plantilla HTML para 
# mostrar en una página web. Por ejemplo, si tienes un objeto Link con la clave "facebook" 
# y el URL "https://www.facebook.com", podrás acceder a ese enlace utilizando ctx['facebook'], 
# que te devolverá "https://www.facebook.com".

from .models import Link

def ctx_dict(request):
    ctx = {}
    links = Link.objects.all()
    for link in links:
        ctx[link.key] = link.url
    return ctx