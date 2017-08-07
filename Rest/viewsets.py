from rest_framework import generics
from rest_framework import viewsets

from .serializers import ProductoSerializer
from Tienda.models import Producto


class ProductoViewset(viewsets.ModelViewSet):
	queryset =  Producto.objects.all()
	serializer_class = ProductoSerializer

