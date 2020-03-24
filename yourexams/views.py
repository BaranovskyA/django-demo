from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone

import yourexams.models as mo
from django.db import connection
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Test, Question, Answer

def show(request, test_id: int):
    test = mo.Test.objects.get(pk=test_id)
    return render(request, 'show.html', context={'test': test})


def index(request):
    logout(request)
    return render(request, 'index.html')

@login_required
def addTest(request):
    if request.method == 'GET':
        return render(request, 'add.html')
    elif request.method == 'POST':
        contextTest = None
        try:
            currTest = mo.Test.objects.get(title=request.POST['title'])

            if currTest.user == request.user:
                newQuestion = mo.Question(text=request.POST['question'], test=currTest)
                newQuestion.save()

                newUnAnswer1 = mo.Answer(text=request.POST['uncorrectAnswer1'], is_correct=False, question=newQuestion)
                newUnAnswer2 = mo.Answer(text=request.POST['uncorrectAnswer2'], is_correct=False, question=newQuestion)
                newUnAnswer3 = mo.Answer(text=request.POST['uncorrectAnswer3'], is_correct=False, question=newQuestion)
                newCorAnswer = mo.Answer(text=request.POST['correctAnswer'], is_correct=True, question=newQuestion)
                newUnAnswer1.save()
                newUnAnswer2.save()
                newUnAnswer3.save()
                newCorAnswer.save()

                newQuestion.answer_set.add(newUnAnswer1)
                newQuestion.answer_set.add(newUnAnswer2)
                newQuestion.answer_set.add(newUnAnswer3)
                newQuestion.answer_set.add(newCorAnswer)

                currTest.question_set.add(newQuestion)
            contextTest = currTest
        except:
            newTest = mo.Test(title=request.POST['title'], date_creating=timezone.now(), ends=0, user=request.user)
            newTest.save()

            newQuestion = mo.Question(text=request.POST['question'], test=newTest)
            newQuestion.save()

            newUnAnswer1 = mo.Answer(text=request.POST['uncorrectAnswer1'], is_correct=False, question=newQuestion)
            newUnAnswer2 = mo.Answer(text=request.POST['uncorrectAnswer2'], is_correct=False, question=newQuestion)
            newUnAnswer3 = mo.Answer(text=request.POST['uncorrectAnswer3'], is_correct=False, question=newQuestion)
            newCorAnswer = mo.Answer(text=request.POST['correctAnswer'], is_correct=True, question=newQuestion)
            newUnAnswer1.save()
            newUnAnswer2.save()
            newUnAnswer3.save()
            newCorAnswer.save()

            newQuestion.answer_set.add(newUnAnswer1)
            newQuestion.answer_set.add(newUnAnswer2)
            newQuestion.answer_set.add(newUnAnswer3)
            newQuestion.answer_set.add(newCorAnswer)
            contextTest = newTest
    questions = []
    if contextTest.user == request.user:
        for t in Test.objects.filter(pk=contextTest.id):
            for q in t.question_set.all():
                questions.append(q.text)
                for a in q.answer_set.all():
                    questions.append(a.text)
        return render(request, 'add.html', context={'test':contextTest, 'questions': questions})
    else:
        return render(request, 'add.html', context={'error': 'Ошибка: данное название уже занято.'})


def reg(request):
    if request.method == 'GET':
        
        return render(request, 'registration.html')
    elif request.method == 'POST':
        if request.POST['password'] != request.POST['repassword']:
            return render(request, 'registration.html', context={'error': 'Ошибка: пароли не совпадают.'})
        user = None
        try:
            mo.User.objects.get(username = request.POST['username']).delete()
            user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
            user.save()
            send_mail('YOUR-EXAMS', '{0}{1}{2}'.format("Дорогой ", request.POST['username'], ", спасибо за регистрацию на нашем сайте."), '1423demon@mail.ru', [request.POST['email']], fail_silently=False)
        except Exception as e:
            print(e)
            
            return render(request, 'registration.html', context={'error': 'Ошибка: пользователь с таким логином или почтой уже существует.'})
        return render(request, 'index.html')
    return render(request, 'index.html')


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect(request.GET.get('next', '/pc'))
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')

@login_required
def pc(request):
    if request.user.is_authenticated:
        tests = []
        for t in Test.objects.filter(user=request.user):
            tests.append(t.title)
        return render(request, 'personalCabinet.html', context={'userLogin': request.user, 'myTests': tests})


def showTest(request):
    return render(request, 'showTest.html')




class TestsView(APIView):
    def get(self, request):
        tests = Test.objects.all()
        return Response({"tests": tests})
