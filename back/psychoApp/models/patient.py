from django.db import models
from . import Therapist


class Patient(models.Model):
    first_name = models.CharField("Nombre", max_length=30)
    last_name = models.CharField("Apellido", max_length=30)
    gender = models.CharField("Género", max_length=50)
    civil_status = models.CharField(
        "Estado cívil", max_length=50, blank=True, null=True
    )
    birthdate = models.DateField(
        "Fecha de Nacimiento", auto_now=False, auto_now_add=False
    )
    education = models.CharField("Educación", max_length=50, blank=True, null=True)
    phone_number = models.CharField(
        "Numero de Telefono", max_length=30, blank=True, null=True
    )
    email = models.CharField("Mail", max_length=30, blank=True, null=True)

    therapist = models.ForeignKey(Therapist, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"
