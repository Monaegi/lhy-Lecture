from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    PERIOD_CHOICES = [(f'{x}', f'{x}기') for x in range(3, 8)]
    USER_TYPE_CHOICES = (
        ('instructor', '강사'),
        ('assistant', '조교'),
        ('manager', '매니저'),
        ('student', '수강생'),
    )

    period = models.CharField(max_length=2, choices=PERIOD_CHOICES, blank=True)
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    img_profile = models.ImageField(upload_to='user', blank=True)

    @property
    def name(self):
        return f'{self.last_name}{self.first_name}'

    def __str__(self):
        if self.period:
            return f'{self.get_period_display()} | {self.name}'
        return f'{self.get_user_type_display()()} | {self.name}'
