# Los formularios de Django son clases

from django import forms


class FormularioPlatos (forms.Form):
    
    # Creando atributo para cargar el selector
    
    Options = (
        (1,'Entrada'),
        (2,'Plato fuerte'),
        (3,'Postre')
    )

    # Dentro de la clase cada atributo será un input

    nombrePlato = forms.CharField(
        widget = forms.TextInput(attrs={'class': 'form-control mb-3'}),
        required = True,
        max_length = 5
    )
    descripcionPlatos = forms.CharField(
        widget = forms.TextInput(attrs={'class': 'form-control mb-3'}),
        required = False,
        max_length = 5
    )
    fotoPlato = forms.CharField(
        widget = forms.TextInput(attrs={'class': 'form-control mb-3'}),
        required = True
    )
    precioPlato = forms.CharField(
        widget = forms.NumberInput(attrs={'class': 'form-control mb-3'}),
        required = True 
    )
    tipoPlato = forms.ChoiceField(
        widget = forms.Select(attrs = {'class':'form-control mb-3'}),
        required = True,
        choices = Options
    )
    
