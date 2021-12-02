from django.contrib import admin
from .models import  Usuario,Paciente,Medico, Administrativo
# Register your models here.
class UsuarioAdmin(admin.ModelAdmin):
    list_display=['rut','dv','nombre','apellido_paterno','apellido_materno','email','telefono_contacto','prevision','usuario_activo']
    search_fields=['nombre','telefono_contacto','email','apellido_paterno','apellido_materno','rut']
    #list_filter=[] #filtros de caracteristicas
    #list_editable=[''] #para poder editar el valor desde el listado 
    list_per_page=50#cantidad de registros por pagina

#admin.site.register(Usuario,UsuarioAdmin)
admin.site.register(Paciente,UsuarioAdmin)
admin.site.register(Medico,UsuarioAdmin)
admin.site.register(Administrativo,UsuarioAdmin)