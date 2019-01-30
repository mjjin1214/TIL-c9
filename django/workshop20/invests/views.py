from django.shortcuts import render
from .models import Question, Choice

# Create your views here.
def detail(request, question_id):
    question = Question.objects.get(pk=question_id)
    return render(request, 'detail.html', {'question':question})
    
def index(request):
    questions = Question.objects.all()
    return render(request, 'index.html', {'questions':questions})
    
def result(request, question_id):
    question = Question.objects.get(pk=question_id)
    choice_id = request.POST.get('choice_id')
    choice = Choice.objects.get(pk=choice_id)
    choice.votes += 1
    choice.save()
    return render(request, 'result.html', {'question':question})