from django.db import models


class Producto(models.Model):
	codigo = models.CharField(primary_key=True,max_length=15)
	name = models.CharField(max_length=20)
	inventario = models.CharField(max_length=5)
	img = models.CharField(max_length=500)


	def __unicode__(self):
		return self.name