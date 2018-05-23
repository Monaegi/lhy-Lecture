from django.contrib.auth.models import AbstractUser
from django.db import models

from utils.mixins import TimeStampedMixin


class User(AbstractUser):
    email = models.EmailField('이메일')
    name = models.CharField('이름', max_length=20)
    img_profile = models.ImageField('프로필 이미지', upload_to='user', blank=True)
    github = models.CharField('GitHub ID', max_length=100, blank=True)
    blog_repository = models.CharField('GitHub 블로그 저장소 이름', max_length=100, blank=True)
    courses = models.ManyToManyField(
        'courses.Course',
        through='Membership',
        related_name='users',
        related_query_name='user',
        blank=True
    )

    # disable exist fields
    first_name = None
    last_name = None

    def __str__(self):
        return f'{self.name}'


class Commit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commits')
    sha = models.CharField('sha', max_length=45)
    message = models.CharField('커밋 메시지', max_length=200)
    url = models.CharField('커밋 URL', max_length=200)
    html_url = models.CharField('커밋 HTML URL', max_length=200)
    created_at = models.DateTimeField()

    def __str__(self):
        return


class Membership(TimeStampedMixin, models.Model):
    MEMBERSHIP_TYPE_CHOICES = (
        ('instructor', '강사'),
        ('assistant', '조교'),
        ('manager', '매니저'),
        ('student', '수강생'),
    )
    user = models.ForeignKey(User, verbose_name='사용자', on_delete=models.CASCADE)
    course = models.ForeignKey('courses.Course', verbose_name='해당 코스', on_delete=models.CASCADE)
    type = models.CharField('사용자 타입', max_length=20, choices=MEMBERSHIP_TYPE_CHOICES)

    def __str__(self):
        return f'{self.course.subject.title}'
