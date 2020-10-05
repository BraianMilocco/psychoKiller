from django.db import models
from . import Patient, Terapist, TemplateTest

class Test(models.Model):
    link = models.CharField("Link", max_length=30)
    result = models.TextField("Resultado", blank=True, null=True)

    terapist = models.ForeignKey(Terapist, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    tenplate_test = models.ForeignKey(TemplateTest, on_delete=models.CASCADE)
    