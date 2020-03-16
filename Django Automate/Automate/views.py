from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from . import automate


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home/')
    else:
        form = UserCreationForm()
    return render(request, 'Register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        form.fields['username'].widget.attrs['class'] = "input100"
        form.fields['password'].widget.attrs['class'] = "input100"
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/home/')
    else:
        form = AuthenticationForm()
        form.fields['username'].widget.attrs['class'] = "input100"
        form.fields['password'].widget.attrs['class'] = "input100"
    return render(request, 'Login.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/login/')


def home_view(request):
    if request.method == 'POST':
        automate.listen()
    return render(request, 'Home.html')