from django.db import models


class Option(models.Model):
    choise = models.TextField("Opción")
    point = models.IntegerField("Puntos", blank=True, null=True)

    def __str__(self):
        return self.choise

    class Meta:
        verbose_name = "Opción"
        verbose_name_plural = "Opciones"
