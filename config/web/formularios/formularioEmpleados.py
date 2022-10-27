# Los formularios de Django son clases

from django import forms

class FormularioEmpleados (forms.Form):
    
    # Creando atributo para cargar el selector
    
    Options = (
        (1,'Mujer'),
        (2,'Hombre')
    )

    # Dentro de la clase cada atributo será un input

    nombreEmpleado = forms.CharField(
        widget = forms.TextInput(attrs={'class': 'form-control mb-3'}),
        required = True,
        max_length = 50
    )
    identificacionEmpleado = forms.CharField(
        widget = forms.NumberInput(attrs={'class': 'form-control mb-3'}),
        required = False,
    )
    fotoEmpleado = forms.CharField(
        widget = forms.TextInput(attrs={'class': 'form-control mb-3'}),
        required = True
    )
    telefonoEmpleado = forms.CharField(
        widget = forms.NumberInput(attrs={'class': 'form-control mb-3'}),
        required = True,
    )
    emailEmpleado = forms.CharField(
        widget = forms.EmailInput(attrs={'class': 'form-control mb-3'}),
        required = True
    )
    generoEmpleado = forms.ChoiceField(
        widget = forms.Select(attrs = {'class':'form-control mb-3'}),
        required = True,
        choices = Options
    )
    