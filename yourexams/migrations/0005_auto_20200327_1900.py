# Generated by Django 3.0.4 on 2020-03-27 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yourexams', '0004_auto_20200325_1715'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='completedtest',
            name='date_creating',
        ),
        migrations.RemoveField(
            model_name='completedtest',
            name='ends',
        ),
        migrations.AddField(
            model_name='completedtest',
            name='correctAnswers',
            field=models.IntegerField(default=0, verbose_name='Количество правильных ответов'),
        ),
    ]
