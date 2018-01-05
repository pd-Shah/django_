from django.contrib import admin
from . import models

class ChoiceInline(admin.TabularInline):
    model=models.Choice
    extra=1

@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines=[ChoiceInline, ]
