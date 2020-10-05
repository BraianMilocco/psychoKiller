from django.db import models
from . import Question, Test, Option

class Answer(models.Model):
    response = models.TextField("Respuesta")

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    option = models.ForeignKey(Option, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return self.response