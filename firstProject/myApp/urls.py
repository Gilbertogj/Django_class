from django.urls import path

from .views import (
    obtener_alumno,
    Alumnos,
    AlumnosList,
    AlumnosDetail,
)

urlpatterns = [
    path("alumnos/", AlumnosList.as_view(), name="alumnos_list"),
    # path("alumnos/<int:id>/", obtener_alumno),
    path("alumnos/<int:pk>/", AlumnosDetail.as_view(), name="alumnos_detail"),
]