from django.contrib import admin


class QuestionAdmin(admin.ModelAdmin):
    list_display = ("template", "number", "query", "question_type")


class TherapistAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "professional_registration", "is_admin")


class TestAdmin(admin.ModelAdmin):
    list_display = ("template_test", "therapist", "patient")


class AnswerAdmin(admin.ModelAdmin):
    list_display = ("test", "question", "response")


class PatientAdmin(admin.ModelAdmin):
    list_display = ("therapist", "first_name", "email", "gender")


class OptionAdmin(admin.ModelAdmin):
    list_display = ("choise", "point")


class TemplateAdmin(admin.ModelAdmin):
    list_display = ("name", "concept")
