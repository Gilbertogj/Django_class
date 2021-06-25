from django.db import models
from django.db.models.deletion import PROTECT
from django.db.models.fields import GenericIPAddressField

# Create your models here.

#alumno 
#first_name   string caracteres
#last_name    string caracteres 
#birthdate    date  string
#gender       string
#email        string 
#phone        number string 
#status       activo, dado de baja
#created_at   
#updated_at
#created_by
#updated_by

class Curso(models.Model):
    """Modelo de Curso"""

    name = models.CharField(max_length=125, unique=True)

    def __str__(self):
        return f"{self.name}"

class Generacion(models.Model):
    """ Modelo de Generacion"""

    numero = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    #Relations
    curso = models.ForeignKey(
        Curso, on_delete=PROTECT, related_name="generaciones"
    )

    def __str__(self):
        return f"{self.numero} curso: {self.curso.name}"


class Mentor(models.Model):
    """Modelo del Mentor"""

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    #Relations
    generaciones= models.ManyToManyField(
        Generacion, related_name="mentores"
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Alumno(models.Model):
    """Alumno modelo"""

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    #Relations
    generacion=models.ForeignKey(
        Generacion, on_delete=models.PROTECT, related_name="alumnos"
    )

    def __str__(self):
        return f"Alumno: {self.first_name} {self.last_name}"




# 1 alumno pertenece a 1 generacion  |  1 generacion - N alumnos -> 1 generacion - N alumnos
# 1 generacion - 1 curso   |   1 curso - N generaciones -> 1 curso - N generaciones 
# 1 mentor - N generacion  |  N generacion - N mentores -> N generacion - N mentores


#one to one   1-1    OneToOneField
#one to many  1-N    ForeignKey
#many to many N-N    ManyToManyField

### ON DELETE ###

#CASCADE- Si elilimo un modelo se eliliminan los datos asocioados a ese modelo 
#PROTECT- No me deja elilimar un modelo si tiene elementos relacionados 




