from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import todo
# Create your views here.

def home(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        new_todo = todo(user=request.user, todo_name=task)
        new_todo.save()
        
    all_todos = todo.objects.filter(user=request.user)
    context = {
        'todos': all_todos
    }   
    return render(request, 'prj_todo/template/todo.html', context)

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if len(password) < 3:
            messages.error(request, 'Password must at least 3 character')
            return redirect('register')
            
        get_all_users_by_username = User.objects.filter(username=username)
        if get_all_users_by_username:
            messages.error(request, 'Error, username already exists, User another.')
            return redirect('register')
             
        new_user = User.objects.create_user(email=email,password=password,username=username)
        new_user.save()
        
        messages.success(request, 'User successfully created, login now')
        return redirect('login')
    return render(request, 'prj_todo/template/register.html',{})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        
        validate_user = authenticate(username=username,password=password)
        if validate_user is not None:
            login(request, validate_user)
            return redirect('home')
        else:
            messages.error(request, 'Error, Wrong user details or user does not exist')
            return redirect('login')
        
    return render(request, 'prj_todo/template/login.html',{})


def DeleteTask(request, name):
    get_todo=todo.objects.get(user=request.user, todo_name=name)
    get_todo.delete()
    return redirect('home')


def Update(request, name):
    get_todo=todo.objects.get(user=request.user, todo_name=name)
    get_todo.status= True
    get_todo.save()
    return redirect('home')