from django.shortcuts import render,redirect
from django.urls import reverse
from django.db.models import Q

from control_foro.models import CrearForo,Forista
from control_foro.forms import ForoFormulario,ForistaFormulario
# Create your views here.

def listar_foros(request):
    foros=CrearForo.objects.all()
    contexto = {
        "foros": foros,
    }
    http_response = render(
        request=request,
        template_name='foros.html',
        context=contexto,
    )
    return http_response

def crear_foro(request):
    if request.method == "POST":
        formulario = ForoFormulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            nombre = data["nombre"]
            tema= data["tema"]
            contenido=data["contenido"]
            foro = CrearForo(nombre=nombre, tema=tema, contenido=contenido)
            foro.save()
            url_exitosa = reverse("vista_foro")
            return redirect(url_exitosa)
    else:  
        formulario = ForoFormulario()
    http_response = render(
        request=request,
        template_name='formulario_foro.html',
        context={'formulario': formulario}
    )
    return http_response

def buscar_foro(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]

        foros = CrearForo.objects.filter(
            Q(nombre__icontains=busqueda) | Q(tema__contains=busqueda)
        )

        contexto = {
            "foros": foros,
        }
        http_response = render(
            request=request,
            template_name='foros.html',
            context=contexto,
        )

        return http_response
    
def crear_forista(request):
    if request.method == "POST":
        formulario = ForistaFormulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            nombre = data["nombre"]
            apellido= data["apellido"]
            sexo=data["sexo"]
            email=data["email"]
            dni=data["dni"]
            fecha_nacimiento=data["fecha_nacimiento"]
            
            
            forista = Forista(nombre=nombre, apellido=apellido, sexo=sexo, email=email, dni=dni, fecha_nacimiento=fecha_nacimiento)
            forista.save()
            url_exitosa = reverse("home")
            return redirect(url_exitosa)
    else:  
        formulario = ForistaFormulario()
    http_response = render(
        request=request,
        template_name='formulario_forista.html',
        context={'formulario': formulario}
    )
    return http_response