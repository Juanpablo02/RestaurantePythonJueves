from django.shortcuts import render

# Create your views here.
# Aqui van los controladores
#Las vistas son funciones de python

def Home(request):
    return render(request,'index.html')