from django.db import models
from . import Terapist


class Patient(models.Model):
    first_name = models.CharField("Nombre", max_length=30)
    last_name = models.CharField("Apellido", max_length=30)
    phone_number = models.CharField(
        "Numero de Telefono", max_length=30, blank=True, null=True
    )
    email = models.CharField("Mail", max_length=30, blank=True, null=True, unique=True)

    terapist = models.ForeignKey(Terapist, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)
