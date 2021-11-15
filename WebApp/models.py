from django.db import models
from django.db.models.deletion import CASCADE

from django.utils import timezone

from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
      DOCTOR = 1
      NURSE = 2
      SURGEN =3
      
      ROLE_CHOICES = (
          (DOCTOR, 'Doctor'),
          (NURSE, 'Nurse'),
          (SURGEN, 'Surgen'),
      )
      role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)
      # You can create Role model separately and add ManyToMany if user has more than one role
    



class Profile(models.Model):
    
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Paciente (models.Model):
    rut=models.IntegerField(null=False, blank=False, unique=True)
    dv=models.IntegerField(null=False, blank=False)
    nombre = models.CharField(max_length=100,null=False, blank=False)
    apellido_paterno=models.CharField(max_length=100,null=False, blank=False)
    apellido_materno=models.CharField(max_length=100,null=False, blank=False)
    correo=models.EmailField(null=True)
    fecha_nacimiento=models.DateField()
    def __int__(self):
        return self.rut
    
class Medico (models.Model):
    rut=models.IntegerField(null=False, blank=False, unique=True)
    dv=models.IntegerField(null=False, blank=False)
    img_perfil=models.ImageField(upload_to='Usuarios', default='blank-profile-picture-973460_640.png')
    def __int__(self):
        return self.rut

#***************CONTACTO ****************************************

opciones_contacto=[
    [0,'RADIOTERAPIA'],
    [1,'RADIOCIRUGÍA'],
    [2,'BRAQUITERAPIA'],
    [3,'FOTODINAMIA'],
    [4,'OTROS']
    ]
class Mensaje(models.Model):
    nombre=models.CharField(max_length=100)
    correo_contacto=models.EmailField(null=False, blank=False)
    tipo_contacto=models.IntegerField(choices=opciones_contacto)
    mensaje=models.TextField()
  

    def __str__(self):
        return self.nombre