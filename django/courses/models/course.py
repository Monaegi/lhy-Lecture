from django.db import models

from utils.mixins import SortableMixin
from utils.models import SortTimeModel

__all__ = (
    'Subject',
    'Course',
)


class Subject(SortTimeModel):
    title = models.CharField(max_length=200)

    class Meta(SortTimeModel.Meta):
        verbose_name = '강의'
        verbose_name_plural = f'{verbose_name} 목록'

    def __str__(self):
        return self.title


class Course(SortTimeModel):
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE,
        related_name='courses',
        related_query_name='course',
    )
    period = models.IntegerField(default=1)

    class Meta(SortTimeModel.Meta):
        verbose_name = '강의 기수'
        verbose_name_plural = f'{verbose_name} 목록'

    def __str__(self):
        return f'{self.subject.title} ({self.period}기)'
