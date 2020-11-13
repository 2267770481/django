from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import UserInfo


# Register your models here.


@admin.register(UserInfo)
class UserProfileAdmin(UserAdmin):
    list_display = ['username', 'password']
    list_per_page = 10

    add_fieldsets = (
        (None, {u'fields': ('username', 'password1', 'password2')}),
        (_('User Information'), {'fields': ('phone', 'gender', 'birthday', 'email')}),
    )
