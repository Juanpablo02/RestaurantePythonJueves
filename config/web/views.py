from django.shortcuts import redirect, render

# Importar el formulario a renderizar

from web.formularios.formularioPlatos import FormularioPlatos
from web.formularios.formularioEmpleados import FormularioEmpleados
from web.models import Platos,Empleado

# Create your views here.
# Aqui van los controladores
# Las vistas son funciones de python

def Home(request):
    return render(request,'index.html')

def ViewPlates(request):
    formulario = FormularioPlatos()
    datosParaTemplate = {
        'formularioRegistro':formulario,
        'bandera':False
    }
    
    # Preguntamos si existe alguna petición de tipo POST asociada a la vista
    if request.method == 'POST':
        # Deberiamos capturar los datos del formulario
        datosFormulario = FormularioPlatos(request.POST)
        # Verificar si los datos llegaron correctamente (Validaciones OK)
        if datosFormulario.is_valid():
            # Capturamos la data
            datosPlatos = datosFormulario.cleaned_data
            # Creamos un objeto de tipo plato
            platoNuevo = Platos(
                nombre_plato = datosPlatos["nombrePlato"],
                descri_plato = datosPlatos["descripcionPlatos"],
                foto_plato = datosPlatos["fotoPlato"],
                precio_plato = datosPlatos["precioPlato"],
                tipo_plato = datosPlatos["tipoPlato"]
            )
            # Intentamos llevar el objeto platoNuevo a La BaseData
            try:
                platoNuevo.save()
                datosParaTemplate['bandera']=True
                print("Exito guardando los datos")
            except Exception as error:
                datosParaTemplate['bandera']=False
                print(f'Error {error}')
        
    return render(request,'platos.html',datosParaTemplate)


def ViewStaff(request):
    formulario = FormularioEmpleados()
    datosParaTemplate = {
        'formularioRegistro':formulario,
        'bandera':False
    }
    if request.method == 'POST':
        datosFormulario = FormularioEmpleados(request.POST)
        if datosFormulario.is_valid():
            datosPersonal = datosFormulario.cleaned_data
            personalNuevo = Empleado(
                nombre_empleado = datosPersonal["nombreEmpleado"],
                apellido_empleado = datosPersonal["apellidoEmpleado"],
                foto_empleado = datosPersonal["fotoEmpleado"],
                cargo_empleado = datosPersonal["cargoEmpleado"],
                salario_empleado = datosPersonal["salarioEmpleado"],
                telefono_empleado = datosPersonal["telefonoEmpleado"],
            )
            try:
                personalNuevo.save()
                datosParaTemplate['bandera']=True
                print("Exito guardando los datos")
            except Exception as error:
                datosParaTemplate['bandera']=False
                print(f'Error {error}')
            
    return render(request,'personal.html',datosParaTemplate)
