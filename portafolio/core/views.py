from django.shortcuts import render, HttpResponse

# Create your views here.

#-------------portada------------
def home(request):
    return render(request, "core/home.html")

#-------------acerca de------------
def about(request):
    return render(request, "core/about.html")

#-------------Portafolio------------
def portafolio(request):
    return render(request, "core/portafolio.html")

#-------------Contacto--------------------
def contact(request):
    return render(request, "core/contacto.html")

#-------------Certificaciones--------------
def certificaciones(request):
    return render(request, "core/certificaciones.html")