from django.db import models
from django.db.models import fields as f, ForeignKey
from django.forms import ChoiceField
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class Test(models.Model):
    title = f.TextField(null=False, max_length=32, verbose_name = _(u'Заголовок'))
    date_creating = f.DateField(auto_now_add=True, verbose_name = _(u'Дата создания'))
    ends = f.IntegerField(default=0, verbose_name = _(u'Количество завершений'))
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name = _(u'Пользователь'))

class Question(models.Model):
    text = f.TextField(verbose_name = _(u'Вопрос'))
    test = ForeignKey(Test, on_delete=models.CASCADE, null=True)

class Answer(models.Model):
    text = f.TextField(verbose_name = _(u'Ответ'))
    is_correct = f.BooleanField(default=False)
    question = ForeignKey(Question, on_delete=models.CASCADE, null=True)