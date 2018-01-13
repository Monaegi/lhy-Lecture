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

    email = models.EmailField('이메일')
    name = models.CharField('이름', max_length=20)
    period = models.CharField('기수', max_length=2, choices=PERIOD_CHOICES, blank=True)
    user_type = models.CharField('사용자 타입', max_length=20, choices=USER_TYPE_CHOICES)
    img_profile = models.ImageField('프로필 이미지', upload_to='user', blank=True)

    # disable exist fields
    first_name = None
    last_name = None

    def __str__(self):
        if self.period:
            return f'{self.get_period_display()} | {self.name}'
        return f'{self.get_user_type_display()} | {self.name}'
