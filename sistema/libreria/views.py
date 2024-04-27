from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    return render(request,"paginas/inicio.html")

def bandeja_solicitudes(request):
    return render(request, "paginas/bandeja_solicitudes.html")

def perfil(request):
    return render(request, "paginas/perfil.html")

def busqueda(request):
    return render(request, "paginas/busqueda.html")

