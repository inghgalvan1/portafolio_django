from django.shortcuts import render, HttpResponse

# Create your views here.

#-------------portada------------
def home(request):
    return render(request, "users/home.html")

#-------------acerca de------------
def about(request):
    return render(request, "users/about.html")

#-------------Portafolio------------
def portafolio(request):
    return render(request, "users/portafolio.html")

#-------------Contacto--------------------
def contact(request):
    return render(request, "users/contacto.html")

#-------------Certificaciones--------------
def certificaciones(request):
    return render(request, "users/certificaciones.html")