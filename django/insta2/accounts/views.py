from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from .forms import CustomForm, CustomChangeForm
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def lists(request):
    users = get_user_model().objects.all()
    return render(request, 'accounts/lists.html', {'users':users})


def signup(request):
    if request.method == 'POST':
        form = CustomForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
        return redirect('accounts:lists')
    else:
        form = CustomForm()
    return render(request, 'accounts/signup.html', {'form':form})
    

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
        return redirect('accounts:lists')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form':form})
    
    
def logout(request):
    auth_logout(request)
    return redirect('accounts:lists')
    
    
def detail(request, user_id):
    person = get_object_or_404(get_user_model(), id=user_id)
    return render(request, 'accounts/detail.html', {'person':person})
    
    
def follow(request, user_id):
    person = get_object_or_404(get_user_model(), id=user_id)
    if request.user in person.followers.all():
        person.followers.remove(request.user)
    else:
        person.followers.add(request.user)
    return redirect('accounts:detail', person.id)
    

def edit(request):
    if request.method == 'POST':
        form = CustomChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:detail', request.user.id)
    else:
        form = CustomChangeForm(instance=request.user)
    return render(request, 'accounts/edit.html', {'form':form})