from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import  Administrativo, Paciente, Usuario,Medico,Administrativo
from django import forms
from import_export import resources
from import_export.admin import ImportExportModelAdmin
class UsuarioAdmin(admin.ModelAdmin):
    list_display=['rut','dv','nombre','apellido_paterno','apellido_materno','email','telefono_contacto','prevision']
    search_fields=['nombre','telefono_contacto','email','apellido_paterno','apellido_materno','rut']
    #list_filter=[] #filtros de caracteristicas
    #list_editable=[''] #para poder editar el valor desde el listado 
    list_per_page=50#cantidad de registros por pagina


class UserCreationForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('rut','email')

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class CustomUserAdmin(ImportExportModelAdmin,UserAdmin):
    # The forms to add and change user instances
    add_form = UserCreationForm
    list_display = ("rut",)
    ordering = ("rut",)

    fieldsets = (
        (None, {'fields': (('rut','dv','password','nombre','apellido_paterno','apellido_materno','email','telefono_contacto','telefono_contacto_2','prevision','fecha_nacimiento','domicilio','type'))}),
        )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('rut','dv','password','nombre','apellido_paterno','apellido_materno','email','telefono_contacto','telefono_contacto_2','prevision','fecha_nacimiento','domicilio','type')}
            ),
        )
    list_filter=[]
    filter_horizontal = ()


admin.site.register(Paciente, CustomUserAdmin)
admin.site.register(Medico, CustomUserAdmin)
admin.site.register(Administrativo, CustomUserAdmin)
  

#admin.site.register(Usuario,UsuarioAdmin)

