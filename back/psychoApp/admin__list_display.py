from django.contrib import admin


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('query', 'question_type', 'template')

class TherapistAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'professional_registration', 'is_admin')