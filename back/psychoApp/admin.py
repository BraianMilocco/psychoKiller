from django.contrib import admin
from .models import Answer, Option, Patient, Question, TemplateTest, Therapist, Test
from .admin__list_display import QuestionAdmin, TherapistAdmin


models_to_register = (Answer, Option, Patient,  TemplateTest, Test)

admin.site.register(models_to_register)


admin.site.register(Question, QuestionAdmin)
admin.site.register(Therapist, TherapistAdmin)