from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.db.models.deletion import CASCADE
from phonenumber_field.modelfields import PhoneNumberField

from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
# Create your models here.


class UsuarioManager(BaseUserManager):
    def create_user(self,email,rut,dv,password=None):
        if not email:
            raise ValueError('Debe Indicar un Email')
        
        usuario=self.model(rut=rut,email=self.normalize_email(email))
        usuario.set_password(password)
        usuario.save()
        return usuario

    def create_superuser(self,email,rut,dv,password):
        usuario=self.create_user(email,rut=rut,dv=dv,password=password)
        usuario.usuario_admin=True
        usuario.save()
        return usuario

class Usuario(AbstractBaseUser):
    email = models.EmailField('Correo Electronico',unique=True)
    nombre=models.CharField('Nombre',max_length=255,null=False)
    apellido_paterno=models.CharField('Apellido Paterno',max_length=255)
    apellido_materno=models.CharField('Apellido Materno',max_length=255)
    rut=models.IntegerField(null=False, blank=False, unique=True)
    #id_student = models.CharField(primary_key=True, max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
    dv=models.CharField(max_length=1,null=False)
    telefono_contacto=PhoneNumberField(null=False, blank=False)
    foto_perfil=models.ImageField('Foto de Perfil',upload_to='Usuarios/',null=True,default='blank-profile-picture-973460_640.png')
    usuario_activo=models.BooleanField(default=True)
    usuario_admin=models.BooleanField(default=False)
    objects=UsuarioManager()
    USERNAME_FIELD='rut'
    REQUIRED_FIELDS=['dv','email']

    def __str__(self):
        return str(self.rut)

    def has_perm(self,perm,obj=None):
        return True
    
    def has_module_perms(self,app_label):
        return True
    @property
    def is_staff(self):
        return self.usuario_admin
    

#******CONTACTO ****************************************

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