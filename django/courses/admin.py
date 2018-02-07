from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin

from .models import (
    Course,
    Subject,
    Section,
    SectionNote,
)


@admin.register(Subject)
class SubjectAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Section)
class SectionAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass


@admin.register(SectionNote)
class SectionNoteAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass


@admin.register(Course)
class CourseAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('subject', 'period',)
