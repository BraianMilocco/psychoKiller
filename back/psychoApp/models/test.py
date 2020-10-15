from django.db import models
from . import Patient, Therapist, TemplateTest


class Test(models.Model):
    link = models.CharField("Link", max_length=30, unique=True)
    result = models.TextField("Resultado", blank=True, null=True)

    therapist = models.ForeignKey(Therapist, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    template_test = models.ForeignKey(TemplateTest, on_delete=models.CASCADE)

    def __str__(self):
        return self.template_test + self.therapist
