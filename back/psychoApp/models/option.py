from django.db import models
from . import Question


class Option(models.Model):
    choise = models.TextField("Opcion")
    point = models.IntegerField("Puntos", blank=True, null=True)

    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.choise
