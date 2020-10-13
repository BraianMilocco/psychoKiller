from django.contrib import admin
from .models import Answer, Option, Patient, Question, TemplateTest, Therapist, Test
from .admin__list_display import (
    QuestionAdmin,
    TherapistAdmin,
    TestAdmin,
    AnswerAdmin,
    PatientAdmin,
    OptionAdmin,
    TemplateAdmin,
)


admin.site.register(Question, QuestionAdmin)
admin.site.register(Therapist, TherapistAdmin)
admin.site.register(Test, TestAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Patient, PatientAdmin)
admin.site.register(Option, OptionAdmin)
admin.site.register(TemplateTest, TemplateAdmin)
