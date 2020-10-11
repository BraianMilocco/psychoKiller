from django.db import models
from . import Patient, Therapist, TemplateTest


class Test(models.Model):
    link = models.CharField("Link", max_length=30)
    result = models.TextField("Resultado", blank=True, null=True)

    therapist = models.ForeignKey(Therapist, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    tenplate_test = models.ForeignKey(TemplateTest, on_delete=models.CASCADE)
