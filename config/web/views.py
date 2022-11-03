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
    
    # Preguntamos si existe alguna petición de tipo POST asociada a la vista
    if request.method == 'POST':
        # Deberiamos capturar los datos del formulario
        datosFormulario = FormularioPlatos(request.POST)
        # Verificar si los datos llegaron correctamente (Validaciones OK)
        if datosFormulario.is_valid():
            # Capturamos la data
            datosPlatos = datosFormulario.cleaned_data
            print(datosFormulario)
            print(datosPlatos)
        
    return render(request,'platos.html',datosParaTemplate)

def Staff(request):
    formulario = FormularioEmpleados()
    datosParaTemplate = {
        'formularioRegistro':formulario
    }
    return render(request,'personal.html',datosParaTemplate)
