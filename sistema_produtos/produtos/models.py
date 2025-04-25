from django.db import models

# Create your models here.
from django.db import models

class Produto(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    disponibilidade = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.marca} {self.modelo}"

