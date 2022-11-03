# Los formularios de Django son clases

from django import forms


class FormularioPlatos (forms.Form):
    
    # Creando atributo para cargar el selector
    
    Options = (
        (1,'Entrada'),
        (2,'Plato fuerte'),
        (3,'Postre'),
        (4,'Coctel'),
        (5,'Bebida gaseosa')
    )

    # Dentro de la clase cada atributo será un input

    nombrePlato = forms.CharField(
        widget = forms.TextInput(attrs={'class': 'form-control mb-3'}),
        required = True,
        max_length = 30,
        label="Nombre del plato"
    )
    descripcionPlatos = forms.CharField(
        widget = forms.TextInput(attrs={'class': 'form-control mb-3'}),
        required = False,
        max_length = 20,
        label="Descripción"
    )
    fotoPlato = forms.CharField(
        widget = forms.TextInput(attrs={'class': 'form-control mb-3'}),
        required = True,
        label="Foto del plato"
    )
    precioPlato = forms.CharField(
        widget = forms.NumberInput(attrs={'class': 'form-control mb-3'}),
        required = True,
        label="Precio del plato" 
    )
    tipoPlato = forms.ChoiceField(
        widget = forms.Select(attrs = {'class':'form-control mb-3'}),
        required = True,
        choices = Options,
        label="Tipo de plato"
    )
    
