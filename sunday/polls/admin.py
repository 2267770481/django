from django.contrib import admin
from .models import Question, Choice
from django.utils.translation import gettext_lazy as _


# @admin.register(Choice)
# class ChoiceAdmin(admin.ModelAdmin):
#     fieldsets = (
#         (None, {'fields': ('choice_text',)}),
#         (_('初始票数'), {'fields': ('votes',)}),
#     )


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('text',)}),
        (_('发布时间'), {'fields': ('date',), 'classes': ['collapse']}),
    )

    inlines = [ChoiceInline]   # 关联 Choice模型类
    list_display = ['text', 'date', 'isNow']
