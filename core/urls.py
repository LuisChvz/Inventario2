from django.urls import path
from .views import home, NuevaCategoria, NuevoProducto, NuevoProducto2, Indice, inventario

urlpatterns = [
    path('', home, name="home"),
]

core_patterns = ([
    path('nuevacategoria', NuevaCategoria.as_view(), name = 'nuevacategoria'),
    path('nuevoproducto', NuevoProducto.as_view(), name = 'nuevoproducto'),
    path('nuevoproducto2', NuevoProducto2.as_view(), name = 'nuevoproducto2'),
    path('indice/<int:categoria>', Indice, name = 'indice'),
    path('inventario/<int:categoria>', inventario, name = 'inventario'),
    
], 'core')