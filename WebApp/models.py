from django.db import models

# Create your models here.

class Usuario (models.Model):
    nombre = models.CharField(max_length=100,null=False, blank=False)
    apellido_paterno=models.CharField(max_length=100,null=False, blank=False)
    apellido_materno=models.CharField(max_length=100,null=False, blank=False)
    rut=models.IntegerField(null=False, blank=False, unique=True)
    dv=models.IntegerField(null=False, blank=False)
    correo=models.EmailField()
    fecha_nacimiento=models.DateField()
    
    img_perfil=models.ImageField(upload_to='Usuarios', default='blank-profile-picture-973460_640.png')
    def __int__(self):
        return self.rut

opciones_contacto=[
    [0,'Consulta'],
    [1,'Reclamo'],
    [2,'Sugerencia'],
    [3,'Felicitaciones']
    ]
class Contacto(models.Model):
    nombre=models.CharField(max_length=100)
    correo=models.EmailField()
    tipo_contacto=models.IntegerField(choices=opciones_contacto)

    def __str__(self):
        return self.nombre