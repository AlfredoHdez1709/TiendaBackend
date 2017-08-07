from rest_framework import serializers
from Tienda.models import Producto

class ProductoSerializer (serializers.HyperlinkedModelSerializer):
	class Meta:
		model= Producto
		fields=('codigo','name','inventario','img')