from django.db import models


class Subject(models.Model):
    title = models.CharField(max_length=200)

    class Meta:
        verbose_name = '강의'
        verbose_name_plural = f'{verbose_name} 목록'

    def __str__(self):
        return self.title


class Course(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    period = models.IntegerField(default=1)

    class Meta:
        verbose_name = '강의 기수'
        verbose_name_plural = f'{verbose_name} 목록'

    def __str__(self):
        return f'{self.subject.title} ({self.period}기)'
