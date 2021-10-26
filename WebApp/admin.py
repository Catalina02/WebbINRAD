from django.contrib import admin
from .models import Mensaje, Usuario,Mensaje

# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):
    list_display=['rut','dv','nombre','apellido_paterno','fecha_nacimiento']
    search_fields=['rut','nombre']
    #list_filter=[] #filtros de caracteristicas
    #list_editable=[''] #para poder editar el valor desde el listado 
    #list_per_page=10#cantidad de registros por pagina



admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Mensaje)