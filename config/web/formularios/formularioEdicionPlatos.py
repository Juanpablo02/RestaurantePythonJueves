
from django import forms


class FormularioEdicionPlatos (forms.Form):
    
    precioPlato = forms.CharField(
        widget = forms.NumberInput(attrs={'class':'form-control mb-3'}),
        required = True,
        label="Precio del plato" 
    )