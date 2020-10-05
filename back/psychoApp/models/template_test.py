from django.db import models


class TemplateTest(models.Model):
    name = models.CharField("Nombre", max_length=30)

    def __str__(self):
        return self.name
