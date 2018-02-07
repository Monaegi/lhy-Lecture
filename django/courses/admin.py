from django.contrib import admin

from .models import (
    Course,
    Subject,
    Section,
    SectionNote,
)


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    pass


@admin.register(SectionNote)
class SectionNoteAdmin(admin.ModelAdmin):
    pass


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('subject', 'period',)
