"""
URL configuration for entrega_3_cesar_peraza project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include

from control_foro.views import listar_foros,crear_foro,buscar_foro,crear_forista
from entrega_3_cesar_peraza.views import inicio_html


urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', inicio_html, name= "home"),
    path('foros/', listar_foros , name="vista_foro"),
    path('crear_foro/', crear_foro , name="para_crear_foro"),
    path('buscar_foro/', buscar_foro , name="para_buscar_foro"),
    path('crear_forista/', crear_forista , name="creacion_forista")
]
