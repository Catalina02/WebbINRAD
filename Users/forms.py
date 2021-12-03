from django import forms
from django.forms import fields
from django.contrib.auth.forms import AuthenticationForm
from Users.models import Usuario

class FormularioUsuario(forms.ModelForm):
    '''
    Formulario de Registro de Usuario Personalizado en BDD
    Variables:
        -password1: Contrasenha
       -password2: Validacion 
    '''
    password1=forms.CharField(label='Contraseña',widget=forms.PasswordInput(
        attrs={
            'class':'form-control',
            'placeholder':'Ingrese su Contraseña...',
            'id':'password1',
            'required':'required'
        }
    ))
    password2=forms.CharField(label='Contraseña de Confirmacion',widget=forms.PasswordInput(
        attrs={
            'class':'form-control',
            'placeholder':'Ingrese nuevamente su Contraseña...',
            'id':'password2',
            'required':'required'
        }
    ))
    class Meta:
        model=Usuario
        fields=('rut','email','nombre','apellido_paterno','apellido_materno')
        widgets={
            'rut':forms.IntegerInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese su RUT'

                }
            ),
            'email':forms.EmailInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Correo Electronico'

                }
            ),      
            'nombre':forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':' Ingrese su Nombre'

            }
            ), 
            'apellido_paterno':forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':' Ingrese su Apellido'

            }
            ),     
            'apellido_materno':forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':' Ingrese su Apellido'

            }
            ),     
        }