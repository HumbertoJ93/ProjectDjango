from django.shortcuts import render, redirect
from .forms import ContactoForm
from django.core.mail import EmailMessage

# Create your views here.
def contacto(request):
    formulario_contacto = ContactoForm
    
    if request.method == 'POST':
        formulario_contacto=formulario_contacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get('nombre')
            correo=request.POST.get('correo')
            contenido=request.POST.get('contenido')
            
            consulta=EmailMessage("Consulta realizada desde el formulario de consultas",
                                  "El usuario {}, realizo la siguiente consulta: {}, responder al correo {}".format(nombre,contenido,correo),
                                  "",
                                  ["ProjectCoderDjango@gmail.com"],
                                  reply_to=[correo])
            try:
                consulta.send()
            
                return redirect('/contacto/?valido')
            except:
                return redirect('/contacto/?novalido')
    
    return render(request, 'contacto/contacto.html', {"formulario_contacto":formulario_contacto})
