from django.shortcuts import render, redirect
from django .http import HttpResponse
from .models import Receta
from .forms import RecetaForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def recetas(request): 
    recetas = Receta.objects.all()
    print(recetas)
    return render(request, 'crud/index.html', {'recetas': recetas})

def crear(request, LoginRequiredMixin):
    formulario = RecetaForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('recetas')
    return render(request, 'crud/crear.html', {'formulario': formulario})

def editar(request, id, LoginRequiredMixin): 
    receta = Receta.objects.get(id=id)
    formulario = RecetaForm(request.POST or None, request.FILES or None, instance=receta)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('recetas')
    return render(request, 'crud/editar.html', {'formulario': formulario})

def eliminar(request, id, LoginRequiredMixin):
    receta = Receta.objects.get(id=id)
    receta.delete()
    return redirect('recetas')

    