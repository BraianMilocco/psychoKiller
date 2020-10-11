from django.db import models
from . import Question, Test


class Option(models.Model):
    choise = models.TextField("Opción")
    point = models.IntegerField("Puntos", blank=True, null=True)

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)

    def __str__(self):
        return self.choise

    class Meta:
        verbose_name = "Opción"
        verbose_name_plural = "Opciones"
        unique_together = ("question", "test")
