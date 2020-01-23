from django.urls import path
from .views import home, NuevaCategoria, NuevoProducto, Indice

urlpatterns = [
    path('', home, name="home"),
]

core_patterns = ([
    path('nuevoproducto', NuevoProducto.as_view(), name = 'nuevoproducto'),
    path('nuevacategoria', NuevaCategoria.as_view(), name = 'nuevacategoria'),
    path('indice/<int:categoria>', Indice, name = 'indice'),
    
], 'core')