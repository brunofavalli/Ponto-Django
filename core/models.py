from django.db import models
from datetime import datetime

# Create your models here.

class Crud(models.Model):
	nome = models.CharField(max_length=50)
	data = models.DateField(default=datetime.now, blank=True)
	entrada = models.TimeField(blank=True)
	saida = models.TimeField(null=True, blank=True)

	def __str__(self):
		return self.nome
