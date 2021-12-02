from django.db import models

# Create your models here.
from django.db import models
from django.db.models.deletion import CASCADE
from phonenumber_field.modelfields import PhoneNumberField
from django.urls import reverse
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import make_password
# Create your models here.

#no olviadar
# id_student = models.CharField(primary_key=True, max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])

#Modificacion a Usuario estandar Django
class UsuarioManager(BaseUserManager):
    
    def create_user(self, rut, email, password=None):

        if rut is None:
            raise TypeError('Debe indicar s RUT')

        if email is None:
            raise TypeError('Debe Indicar su Email')

        usuario = Usuario.objects.create(
        email=email,
        rut=rut,
        password = make_password(password))

        return usuario

    def create_superuser(self,email,rut,dv,password):
        usuario=self.create_user(rut,email,password=password)
        usuario.usuario_admin=True
        usuario.save()
        return usuario

class Usuario(AbstractBaseUser):
    rut=models.IntegerField(null=False, blank=False, unique=True)
    dv=models.CharField(max_length=1,null=False)
    
    nombre=models.CharField('Nombre',max_length=100,null=False)
    apellido_paterno=models.CharField('Apellido Paterno',max_length=100)
    apellido_materno=models.CharField('Apellido Materno',max_length=100)
    
    email = models.EmailField('Correo Electronico',unique=True)
    telefono_contacto=PhoneNumberField(null=False, blank=False)
    telefono_contacto_2=PhoneNumberField(null=True, blank=True,default='+56900000000')
    fecha_nacimiento=models.DateField(null=True)
    
    prevision=models.CharField('Prevision',max_length=50,null=False)
    domicilio=models.CharField('Domicilio',max_length=255,null=False)

    foto_perfil=models.ImageField('Foto de Perfil',upload_to='Usuarios/',null=True,default='blank-profile-picture-973460_640.png')

    usuario_activo=models.BooleanField(default=True)
    usuario_admin=models.BooleanField(default=False)
    

    #definir los tipos de usuarios
    class Types(models.TextChoices):
        Paciente='Paciente','PACIENTE'
        Medico='Medico','MEDICO'
        Administrativo='Administrativo','ADMINISTRATIVO'
        
    type=models.CharField(_('Tipo de Usuario'),choices=Types.choices, default=Types.Paciente,max_length=100)

    

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
    
#Definir tipos de Usuarios
class PacienteManager(models.Manager):
    def get_queryset(self,*args,**kwargs): 
        return super().get_queryset(*args,*kwargs).filter(type=Usuario.Types.Paciente)
class Paciente(Usuario):
    objects=PacienteManager()
    class Meta:
        proxy=True
    def save(self, *args,**kwargs):
        if not self.pk:
            self.type=Usuario.Paciente
        return super().save(*args,**kwargs)

class MedicoManager(models.Manager):
    def get_queryset(self,*args,**kwargs): 
        return super().get_queryset(*args,*kwargs).filter(type=Usuario.Types.Medico)    
class Medico(Usuario):
    objects=MedicoManager()
    class Meta:
        proxy=True
    def save(self, *args,**kwargs):
        if not self.pk:
            self.type=Usuario.Medico
        return super().save(*args,**kwargs)

class AdministrativoManager(models.Manager):
    def get_queryset(self,*args,**kwargs): 
        return super().get_queryset(*args,*kwargs).filter(type=Usuario.Types.Administrativo)    
class Administrativo(Usuario):
    objects=AdministrativoManager()
    class Meta:
        proxy=True
    def save(self, *args,**kwargs):
        if not self.pk:
            self.type=Usuario.Administrativo
        return super().save(*args,**kwargs)
