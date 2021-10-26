from django import forms
from .models import Mensaje, Mensaje

class MensajeForm(forms.ModelForm):
    class Meta:
        #obtiene tipos de datos desde el modelo definido
        model=Mensaje
        #fields=['nombre','correo_contacto','tipo_contacto','mensaje']
        fields='__all__'