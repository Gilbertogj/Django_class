from django.urls import path

from .views import (
    obtener_alumno,
    Alumnos,
    AlumnosList,
    AlumnosDetail,
    AlumnosCreate,
    AlumnosUpdate,
)

urlpatterns = [
    path("alumnos/", AlumnosList.as_view(), name="alumnos_list"),
    path("alumnos/create/", AlumnosCreate.as_view(), name="alumnos_create"),
    path("alumnos/<int:pk>/update/", AlumnosUpdate.as_view(), name="alumnos_update"),
    # path("alumnos/<int:id>/", obtener_alumno),
    path("alumnos/<int:pk>/", AlumnosDetail.as_view(), name="alumnos_detail"),
]