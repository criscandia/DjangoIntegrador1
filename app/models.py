from django.db import models

# Create your models here.

TALLE_CHOISE = (
    (1, " Extra Small"),
    (2, "Small"),
    (3, "Medium"),
    (4, "Large"),
    (5, "Extra Large"),
    (6, "Super Extra Large")

)

GENERO_CHOISE = (
    (1, "Hombre"),
    (2, "Mujer"),
    (3, "Unisex"),
)

class Remeras(models.Model):
    marca = models.CharField(max_length=100)
    talle = models.IntegerField(choices=TALLE_CHOISE, default=1, null=True)
    color = models.CharField(max_length=100)
    lisa = models.BooleanField(null=True)
    genero = models.IntegerField(choices=GENERO_CHOISE, default=1, null=True)
