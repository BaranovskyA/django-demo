from django.db import models
from django.db.models import fields as f, ForeignKey
from django.forms import ChoiceField
from django.contrib.auth.models import User

class Test(models.Model):
    title = f.TextField(null=False, max_length=32)
    date_creating = f.DateField(auto_now_add=True)
    ends = f.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class Question(models.Model):
    text = f.TextField()
    test = ForeignKey(Test, on_delete=models.CASCADE, null=True)

class Answer(models.Model):
    text = f.TextField()
    is_correct = f.BooleanField(default=False)
    question = ForeignKey(Question, on_delete=models.CASCADE, null=True)