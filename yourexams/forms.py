from django import forms


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=24)
    password = forms.CharField(max_length=24)
    repassword = forms.CharField(max_length=24)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=24)
    password = forms.CharField(max_length=24)


class TestForm(forms.Form):
    title = forms.CharField(max_length=32)
    question = forms.CharField(max_length=32)
    correctAnswer = forms.CharField(max_length=32)
    uncorrectAnswer1 = forms.CharField(max_length=32)
    uncorrectAnswer2 = forms.CharField(max_length=32)
    uncorrectAnswer3 = forms.CharField(max_length=32)
