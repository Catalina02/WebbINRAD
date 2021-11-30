from django.contrib import admin
from .models import Mensaje, Usuario#, Paciente,Mensaje,Medico,Profile,User

from import_export import resources
from import_export.admin import ImportExportModelAdmin



#Aciiones
def marcar_contacto(modeladmin, request, queryset):
    queryset.update(paciente_contactado=True)

marcar_contacto.short_description = 'Marcar Usuarios que ya han sido Contactados'
# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):
    list_display=['rut','dv','nombre','apellido_paterno','apellido_materno','email','telefono_contacto','prevision','usuario_activo']
    search_fields=['nombre','telefono_contacto','email','apellido_paterno','apellido_materno','rut']
    #list_filter=[] #filtros de caracteristicas
    #list_editable=[''] #para poder editar el valor desde el listado 
    list_per_page=50#cantidad de registros por pagina
class ContactoAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=['nombre','telefono_contacto','correo_contacto','tipo_contacto','mensaje','paciente_contactado','fecha_contacto']
    list_filter=['tipo_contacto','paciente_contactado','fecha_contacto']
    search_fields=['nombre','telefono_contacto','correo_contacto','tipo_contacto']
    list_editable=['paciente_contactado']
    list_per_page=50

    actions = [marcar_contacto]
    #resource_class=MensajeResource

#admin.site.register(Paciente, UsuarioAdmin)
#admin.site.register(Medico)
#admin.site.register(Profile)
admin.site.register(Mensaje,ContactoAdmin)
admin.site.register(Usuario,UsuarioAdmin)