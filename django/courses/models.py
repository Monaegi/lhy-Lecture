from django.db import models
from martor.models import MartorField


class Subject(models.Model):
    title = models.CharField(max_length=200)

    class Meta:
        verbose_name = '강의'
        verbose_name_plural = f'{verbose_name} 목록'

    def __str__(self):
        return self.title


class Section(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, blank=True, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = '강의 섹션'
        verbose_name_plural = f'{verbose_name} 목록'

    def __str__(self):
        if self.subject:
            return f'{self.subject.title} | {self.title}'
        return f'{self.title}'


class SectionNote(models.Model):
    section = models.ForeignKey(Section, on_delete=models.SET_NULL, blank=True, null=True)
    title = models.CharField(max_length=100)
    content = MartorField(blank=True)

    class Meta:
        verbose_name = '섹션 노트'
        verbose_name_plural = f'{verbose_name} 목록'

    def __str__(self):
        if self.section:
            return f'{self.section.__str__()} | {self.title}'
        return f'{self.title}'


class Course(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    period = models.IntegerField(default=1)

    class Meta:
        verbose_name = '강의 기수'
        verbose_name_plural = f'{verbose_name} 목록'

    def __str__(self):
        return f'{self.subject.title} ({self.period}기)'
