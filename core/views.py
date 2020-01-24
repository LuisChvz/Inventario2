from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from braces.views import SuperuserRequiredMixin, LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .forms import NuevaCategoriaForm, NuevoProductoForm, NuevoProductoForm2
from .models import Categoria, Producto, Entrada, Salida



@login_required
def home(request):
    return render(request, "core/home.html")

class NuevaCategoria(SuperuserRequiredMixin, CreateView):
    model = Categoria
    form_class = NuevaCategoriaForm
    success_url = reverse_lazy('core:indice', args=[0])


class NuevoProducto(LoginRequiredMixin, CreateView):
    model = Producto
    form_class = NuevoProductoForm
    success_url = reverse_lazy('core:indice', args=[0])
    
class NuevoProducto2(LoginRequiredMixin, CreateView):
    model = Producto
    form_class = NuevoProductoForm2
    success_url = reverse_lazy('core:indice', args=[0])
 
    
def Indice(request, categoria):
    filtro = categoria
    categorias = Categoria.objects.all()
    
    if filtro == 0:
        productos = Producto.objects.all()
    else:
        productos = Producto.objects.filter(categoria = filtro)
        
    return render(request, 'core/indice.html', {'categorias': categorias, 'productos': productos, 'filtro':filtro})

def inventario(request, categoria):
    filtro = categoria
    categorias = Categoria.objects.all()
    
    if filtro == 0:
        productos = Producto.objects.all()
    else:
        productos = Producto.objects.filter(categoria = filtro)
        
    return render(request, 'core/inventario.html', {'categorias': categorias, 'productos': productos, 'filtro':filtro})
    
