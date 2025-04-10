"""
URL configuration for Pruebas1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from myapp import views #ya que el segundo argumento del path es una vista, tengo que importar la vista que quiero usar. osea la funcion index

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"), #el primer argumento es la URL que quiero que se muestre, el segundo argumento es la vista que quiero usar y el tercer argumento es el nombre de la URL.
]
#ante la solucitud "" (que aparece en la barra del buscador), responde con la funcion index de la vista views.py
#el nombre de la URL es opcional, pero es recomendable ponerlo para poder referenciarlo en otras partes del proyecto