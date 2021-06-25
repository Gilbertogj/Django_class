from django.urls import path

from .views import (bienvenida,
    despedida, 
    saludo, 
    saludo_nombre, 
    website_call, 
    lista_alumnos, 
    alumnos,
    obtener_alumno
)

urlpatterns = [
    path("", bienvenida),
    path("despedida/", despedida),
    path("saludo/", saludo),
    path("saludo/<str:first_name>/", saludo_nombre),
    path("liga/<str:website>/", website_call),
    path("lista_alumnos/",lista_alumnos ),
    path("alumnos/",alumnos ),
    path("alumnos/<int:id>/",obtener_alumno),
]