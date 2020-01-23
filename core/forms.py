from django import forms
from core.models import Categoria, Producto, Entrada, Salida
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class NuevaCategoriaForm(forms.ModelForm):
    
    class Meta: 
        model = Categoria
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre: '}),
        }
        labels = {
            'nombre':''
        }

class CategoriaModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, Categoria):
        return Categoria.nombre

class NuevoProductoForm(forms.ModelForm):
    categoria =  CategoriaModelChoiceField(queryset = Categoria.objects.filter().order_by('id'), required = True, widget = forms.Select(attrs={'class':'form-control'}))
    
    class Meta: 
        model = Producto
        fields = ['nombre','categoria', 'unidadPaquete']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre: '}),
            'unidadPaquete': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Precio unitario: '}),
        }
        labels = {
             'nombre':'Nombre', 'unidadPaquete':'Unidades por paquete', 'categoria':'Categoria'
        }