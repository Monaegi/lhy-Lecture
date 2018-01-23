from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

from .models import User


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    list_display = ('name', 'email',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('기본정보', {'fields': ('name', 'email')}),
        ('추가정보', {'fields': ('period', 'user_type', 'img_profile')}),
        ('중요날짜', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2',),
        }),
        ('필수정보', {
            'classes': ('wide',),
            'fields': ('name', 'email', 'user_type',),
        }),
        ('추가정보', {
            'classes': ('wide',),
            'fields': ('period', 'img_profile',),
        }),
    )
    ordering = ('name',)
