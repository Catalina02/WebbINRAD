from django.shortcuts import render
from .forms import  MensajeForm

def home(request):
    return render(request, 'base.html')

def contacto(request):
    data={
        'form':MensajeForm()
    }
    if request.method=='POST':# si se reciben datos del formulario
        formulario=MensajeForm(data=request.POST) #entrega lo que hat en post(datos de formularp)
        if formulario.is_valid():
            formulario.save()
            data['mensaje']='Mensaje Guardado'
        else:
            data['form']=formulario

    return render(request,'contacto.html',data)
 
def nosotros(request):
    return render(request,'nosotros.html')
 
def tratamientos(request):
    return render(request,'tratamientos.html')
 
def pacientes(request):
    return render(request,'pacientes.html')
 
def login(request):
    return render(request,'login.html')
 
def registro(request):
    return render(request,'registro.html')
 