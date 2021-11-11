from django.db import models

# Create your models here.

class Paciente (models.Model):
    rut=models.IntegerField(null=False, blank=False, unique=True)
    dv=models.IntegerField(null=False, blank=False)
    nombre = models.CharField(max_length=100,null=False, blank=False)
    apellido_paterno=models.CharField(max_length=100,null=False, blank=False)
    apellido_materno=models.CharField(max_length=100,null=False, blank=False)
    correo=models.EmailField(null=True)
    fecha_nacimiento=models.DateField()
    

    
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