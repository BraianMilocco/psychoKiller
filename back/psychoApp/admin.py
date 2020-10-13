from django.contrib import admin
from .models import Answer, Option, Patient, Question, TemplateTest, Therapist, Test

models_to_register = (Answer, Option, Patient, Question, TemplateTest, Therapist, Test)
admin.site.register(models_to_register)
