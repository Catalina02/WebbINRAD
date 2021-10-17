from django.shortcuts import render

def home(request):
    return render(request, 'base.html')

def contacto(request):
    return render(request,'contacto.html')
 
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
 