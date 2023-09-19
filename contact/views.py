from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.
def contact(request):
    contact_form = ContactForm()# Se crea la plantilla vacia
    
    if request.method == "POST":# Verificamos si se a mandado por POST un dato
        contact_form = ContactForm(data=request.POST)# LLenamos la plantilla con esta informacion 
        if contact_form.is_valid():# Si son correcto
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')# Tenemos toda la estructura
            # Enviamos correo y redireccionamos
            email = EmailMessage(
                "La Caffettiera: Nuevo mensaje de correo",
                "De {} <{}>\n\nEscribió:\n\n{}".format(name,email,content),
                "no-contestar@inbox.mailtrap.io",
                ["salgadoibacache.s@gmail.com"],
                reply_to=[email]
            )
            try:
                email.send()# Si todo resulta bien, redirecionamos a ok
                return redirect(reverse('contact')+"?ok")
            except:
                return redirect(reverse)# Si no salio bien, redireccionamos a FAIL
            return redirect(reverse('contact')+"?fail")
        
    return render(request, "contact/contact.html", {'form': contact_form})