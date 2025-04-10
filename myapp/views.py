from django.shortcuts import render

# Create your views here.

def index(request):
    context = {"mensaje": "Bienvenidos a mi aplicacion hecha en Django" } #la clave es lo que se le pasa al HTML, el valor es lo que quiero que se pase al HTML como contenido
    return render(request, "myapp/index.html", context) #render es una funcion que recibe el request, el nombre de la plantilla y el contexto