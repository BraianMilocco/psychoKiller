from django.db import models
from . import TemplateTest


class Question(models.Model):
    CLOSE = "CL"
    OPEN = "OP"
    QUESTION_TYPE_OPTIONS = [
        (CLOSE, "Cerrada"),
        (OPEN, "Abierta"),
    ]

    query = models.TextField("Enunciado")
    question_type = models.CharField(
        "Tipo de Pregunta", max_length=2, choices=QUESTION_TYPE_OPTIONS, default=OPEN
    )

    template = models.ForeignKey(TemplateTest, on_delete=models.CASCADE)

    def __str__(self):
        return self.query
