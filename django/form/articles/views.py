from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleModelForm
# workshop 26
# from .models import Student
# from .forms import StudentForm

# Create your views here.
def create(request):
    if request.method == 'POST':
        form = ArticleModelForm(request.POST)
        if form.is_valid():
            article = form.save()
            # title = form.cleaned_data.get('title')
            # content = form.cleaned_data.get('content')
            # article = Article(title=title, content=content)
            # article.save()
            # article = Article.objects.create(title=title, content=content)
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleModelForm()
        
    return render(request, 'form.html', {'form':form})
        
        
def detail(request, article_id):
    article = Article.objects.get(pk=article_id)
    return render(request, 'detail.html', {'article':article})
    

def update(request, article_id):
    article = Article.objects.get(pk=article_id)
    if request.method == 'POST':
        form = ArticleModelForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleModelForm(instance=article)
        
    return render(request, 'form.html', {'form':form})
    
# workshop 26    
# def create(request):
#     if request.method == 'POST':
#         form = StudentForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data.get('name')
#             age = form.cleaned_data.get('age')
#             student = Student.objects.create(name=name, age=age)
#             return redirect('studentinfo', student.pk)
#     else:
#         form = StudentForm()
#     return render(request, 'new.html', {'form':form})
    
    
# def studentinfo(request, student_id):
#     student = Student.objects.get(pk=student_id)
#     return render(request, 'studentinfo.html', {'student':student})