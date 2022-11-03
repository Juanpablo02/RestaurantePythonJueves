# Los formularios de Django son clases

from django import forms

class FormularioEmpleados (forms.Form):
    
    # Creando atributo para cargar el selector
    
    Options = (
        (1,'Cocinero'),
        (2,'Auxiliar'),
        (3,'Mesero'),
        (4,'Administrador')
    )

    # Dentro de la clase cada atributo será un input

    nombreEmpleado = forms.CharField(
        widget = forms.TextInput(attrs={'class': 'form-control mb-3'}),
        required = True,
        max_length = 50,
        label = "Nombres del empleado"
    )
    apellidoEmpleado = forms.CharField(
        widget = forms.TextInput(attrs={'class': 'form-control mb-3'}),
        required = True,
        max_length = 50,
        label = "Apellidos del empleado"
    )
    fotoEmpleado = forms.CharField(
        widget = forms.TextInput(attrs={'class': 'form-control mb-3'}),
        required = True,
        label = "Foto del empleado"
    )
    cargoEmpleado = forms.ChoiceField(
        widget = forms.Select(attrs = {'class':'form-control mb-3'}),
        required = True,
        choices = Options,
        label = "Cargo del empleado"
    )
    salarioEmpleado = forms.CharField(
        widget = forms.NumberInput(attrs={'class': 'form-control mb-3'}),
        required = True,
        label = "Salario del empleado"
    )
    telefonoEmpleado = forms.CharField(
        widget = forms.NumberInput(attrs={'class': 'form-control mb-3'}),
        required = True,
        label = "Número de contacto"
    )
    
    