from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from django.template import context, loader
from .models import Alumno

def bienvenida(request):

    return HttpResponse("<h1>Bienvenidos<h1> <h3>alumnos<h3>")


def despedida(request):
    return HttpResponse("Adiós alumnos")

def saludo(request):
    color = 'style="color: red "'
    url="https://google.com"
    text= f"<a {color} href={url}> Hola</a>"
    return HttpResponse(text)

def saludo_nombre(request,first_name):
    ## Datos de la DB
    context = {
        "name": first_name,
        "last_name": "GARCIA jasso skdksd "
    }
    template= loader.get_template("saludo_nombre.html")

    return HttpResponse (template.render(context,request))


def lista_alumnos(request):
    context = {
        "curso": {
            "name":"Django",
            "generation": "1",
            "profesores": ["Gil", "Juan"],
        },
        "alumnos": [
            {
                "first_name": "Ana",
                "last_name":"Ponce",
                "isActive": True,
            },
            {
                "first_name": "Ale",
                "last_name": "Flores",
                "isActive": True,
            },
            {
                "first_name": "Oscar",
                "last_name": "Altamirano",
                "isActive": True,
            },
            {
                "first_name": "Pedro",
                "last_name": "Rivas",
                "isActive": False,
            },
        ]
    }
    template= loader.get_template("list_alumnos.html")
    return HttpResponse (template.render(context,request))

def alumnos(request):
    context = {
        "alumnos": [
            {
                "first_name": "Ana",
                "last_name":"Ponce",
                "isActive": True,
            },
            {
                "first_name": "Ale",
                "last_name": "Flores",
                "isActive": True,
            },
            {
                "first_name": "Oscar",
                "last_name": "Altamirano",
                "isActive": True,
            },
            {
                "first_name": "Pedro",
                "last_name": "Rivas",
                "isActive": False,
            },
        ]
    }
    template= loader.get_template("myApp/list.html")
    return HttpResponse (template.render(context,request))

def obtener_alumno(request,id):
    """Esta vista mostrará un alumno dado su ID"""
    alumno = Alumno.objects.get(id=id)
    context ={"alumno":alumno}

    # alumnos= [
    #     {
    #         "id":1,
    #         "first_name": "Ana",
    #         "last_name":"Ponce",
    #         "isActive": True,
    #     },
    #     {
    #         "id":2,
    #         "first_name": "Ale",
    #         "last_name": "Flores",
    #         "isActive": True,
    #     },
    #     {
    #         "id":3,
    #         "first_name": "Oscar",
    #         "last_name": "Altamirano",
    #         "isActive": True,
    #     },
    #     {
    #         "id":4,
    #         "first_name": "Pedro",
    #         "last_name": "Rivas",
    #         "isActive": False,
    #     },
    # ]
    # context = {}
    # for alumno in alumnos:
    #     if alumno['id'] == id:
    #         context['alumno']=alumno
    
    template= loader.get_template("myApp/get_alumnos.html")
    return HttpResponse (template.render(context,request))




















def website_call(request,website):
    url= f'<a href="https://{website}.com" > liga </a>'   
    return HttpResponse (url)