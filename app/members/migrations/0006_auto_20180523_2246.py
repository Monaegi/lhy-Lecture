# Generated by Django 2.0.5 on 2018-05-23 13:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_auto_20180123_2110'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sha', models.CharField(max_length=45, verbose_name='sha')),
                ('message', models.CharField(max_length=200, verbose_name='커밋 메시지')),
                ('url', models.CharField(max_length=200, verbose_name='커밋 URL')),
                ('html_url', models.CharField(max_length=200, verbose_name='커밋 HTML URL')),
                ('created_at', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='blog_repository',
            field=models.CharField(blank=True, max_length=100, verbose_name='GitHub 블로그 저장소 이름'),
        ),
        migrations.AddField(
            model_name='user',
            name='github',
            field=models.CharField(blank=True, max_length=100, verbose_name='GitHub ID'),
        ),
        migrations.AddField(
            model_name='commit',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commits', to=settings.AUTH_USER_MODEL),
        ),
    ]
