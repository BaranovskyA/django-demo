# Generated by Django 3.0.4 on 2020-03-27 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yourexams', '0005_auto_20200327_1900'),
    ]

    operations = [
        migrations.AddField(
            model_name='completedtest',
            name='maxCorrectAnswers',
            field=models.IntegerField(default=0, verbose_name='Количество правильных ответов'),
        ),
    ]