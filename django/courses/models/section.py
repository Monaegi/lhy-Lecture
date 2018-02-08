from django.db import models
from martor.models import MartorField

from utils.models import SortTimeModel
from .course import Subject

__all__ = (
    'Section',
    'SectionNote',
)


class Section(SortTimeModel):
    subject = models.ForeignKey(
        Subject, on_delete=models.SET_NULL,
        related_name='sections',
        related_query_name='section',
        blank=True, null=True,
    )
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    class Meta(SortTimeModel.Meta):
        verbose_name = '강의 섹션'
        verbose_name_plural = f'{verbose_name} 목록'

    def __str__(self):
        if self.subject:
            return f'{self.subject.title} | {self.title}'
        return f'{self.title}'


class SectionNote(SortTimeModel):
    section = models.ForeignKey(
        Section, on_delete=models.SET_NULL,
        related_name='notes',
        related_query_name='note',
        blank=True, null=True,
    )
    title = models.CharField(max_length=100)
    content = MartorField(blank=True)

    class Meta(SortTimeModel.Meta):
        verbose_name = '섹션 노트'
        verbose_name_plural = f'{verbose_name} 목록'

    def __str__(self):
        if self.section:
            return f'{self.section.__str__()} | {self.title}'
        return f'{self.title}'
