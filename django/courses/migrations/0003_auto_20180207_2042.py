# Generated by Django 2.0.1 on 2018-02-07 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20180207_1721'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['_order'], 'verbose_name': '강의 기수', 'verbose_name_plural': '강의 기수 목록'},
        ),
        migrations.AlterModelOptions(
            name='section',
            options={'ordering': ['_order'], 'verbose_name': '강의 섹션', 'verbose_name_plural': '강의 섹션 목록'},
        ),
        migrations.AlterModelOptions(
            name='sectionnote',
            options={'ordering': ['_order'], 'verbose_name': '섹션 노트', 'verbose_name_plural': '섹션 노트 목록'},
        ),
        migrations.AlterModelOptions(
            name='subject',
            options={'ordering': ['_order'], 'verbose_name': '강의', 'verbose_name_plural': '강의 목록'},
        ),
        migrations.AddField(
            model_name='course',
            name='_order',
            field=models.PositiveIntegerField(default=0, verbose_name='순서'),
        ),
        migrations.AddField(
            model_name='section',
            name='_order',
            field=models.PositiveIntegerField(default=0, verbose_name='순서'),
        ),
        migrations.AddField(
            model_name='sectionnote',
            name='_order',
            field=models.PositiveIntegerField(default=0, verbose_name='순서'),
        ),
        migrations.AddField(
            model_name='subject',
            name='_order',
            field=models.PositiveIntegerField(default=0, verbose_name='순서'),
        ),
    ]