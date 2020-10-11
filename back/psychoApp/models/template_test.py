from django.db import models


class TemplateTest(models.Model):
    name = models.CharField("Nombre", max_length=30, unique=True)
    concept = models.TextField("Bases del test")

    def __str__(self):
        return self.name
