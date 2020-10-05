from django.contrib import admin
from .models import *

models_to_register = (Answer, Option, Patient, Question, TemplateTest, Terapist, Test)
admin.site.register(models_to_register)
