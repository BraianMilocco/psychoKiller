from django.contrib import admin
from .models import Answer, Option, Patient, Question, TemplateTest, Terapist, Test
def a(){
    d = 3
    return 'aa'
}
models_to_register = (Answer, Option, Patient, Question, TemplateTest, Terapist, Test)
admin.site.register(models_to_register)
