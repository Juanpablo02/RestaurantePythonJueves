from django.shortcuts import redirect, render

# Importar el formulario a renderizar

from web.formularios.formularioPlatos import FormularioPlatos
from web.formularios.formularioEmpleados import FormularioEmpleados

# Create your views here.
# Aqui van los controladores
#Las vistas son funciones de python

def Home(request):
    return render(request,'index.html')

def Plates(request):
    formulario = FormularioPlatos()
    datosParaTemplate = {
        'formularioRegistro':formulario
    }
    return render(request,'platos.html',datosParaTemplate)

def Staff(request):
    formulario = FormularioEmpleados()
    datosParaTemplate = {
        'formularioRegistro':formulario
    }
    return render(request,'personal.html',datosParaTemplate)
