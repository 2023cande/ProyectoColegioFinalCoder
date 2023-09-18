from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Alumno(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()

    def __str__ (self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Email: {self.email}"

class Profesor(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    materia= models.CharField(max_length=30)

    def __str__ (self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Email: {self.email} - Materia: {self.materia} "

class Entregables(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    fechaDeEntrega = models.DateField()  


    def __str__ (self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - FechaDeEntrega: {self.fechaDeEntrega}"


class Avatar(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares' , null=True , blank=True)

    
