from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from django.template import context, loader
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import FormView, UpdateView
from django.urls import reverse_lazy

from .models import Alumno
from .forms import AlumnoForm


#Vistas para alumnos

def lista_alumnos(request):
    """Lista de alumnos basada en funcion"""
    alumnos=Alumno.objects.all()  
    context={"alumnos":alumnos}
    template= loader.get_template("myApp/list_alumnos.html")
    return HttpResponse(template.render(context,request))


def obtener_alumno(request,id):
    """Obtener alumno dependiedo su id"""
    alumno=Alumno.objects.get(id=id)
    context={"alumno":alumno}
    template= loader.get_template("myApp/get_alumnos.html")
    return HttpResponse(template.render(context,request))


#Vistas basadas en clases

class Alumnos(View):
    def get(self,request):
        alumnos=Alumno.objects.all()  
        context={"alumnos":alumnos}
        template= loader.get_template("myApp/list_alumnos.html")
        return HttpResponse(template.render(context,request))


# class AlumnosList(TemplateView):
#     template_name="myApp/list_alumnos.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         print(context,  'Esto hereda del padre' )
#         context["alumnos"] = Alumno.objects.all() 
#         print(context, 'este es el que sobrescribimos ')
#         return context

## Generic Views##

class AlumnosList (ListView):
    model = Alumno
    template_name = "myApp/list_alumnos.html"
    context_object_name = "alumnos"


class AlumnosDetail (DetailView):
    model = Alumno
    template_name = "myApp/get_alumnos.html"
    context_object_name = "alumno"


class AlumnosCreate(CreateView):
    template_name = "myApp/create_alumnos.html"
    form_class = AlumnoForm
    success_url = reverse_lazy("myapp:alumnos_list")

class AlumnosUpdate(UpdateView):
    model = Alumno
    template_name = "myApp/update_alumnos.html"
    form_class = AlumnoForm
    success_url = reverse_lazy("myapp:alumnos_list")
















































