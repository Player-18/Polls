from django.contrib import admin

from .models import Question, Choice


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'question_text', 'pub_date')
    empty_value_display = "-пусто-"


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('pk', 'question', 'choice_text', 'votes')
    empty_value_display = "-пусто-"


admin.site.register(Question)
admin.site.register(Choice)