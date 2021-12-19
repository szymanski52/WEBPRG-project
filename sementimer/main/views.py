from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegistrationForm, SearchForm
import os


def render_main(request):
    return render(request, 'main/main.html')


def render_auth(request):
    context = {'user_form': UserRegistrationForm(), 'form': AuthenticationForm()}
    return render(request, 'main/auth.html', context)


def render_profile(request):
    context = {}

    return render(request, 'main/profile.html', context)


def render_messages(request):
    context = {}

    return render(request, 'main/messages.html', context)


def render_contacts(request):
    context = {}

    return render(request, 'main/contacts.html', context)


def search(request):
    context = {}
    if request.method == 'POST':
        search_form = SearchForm(request.POST)
        users = User.objects.filter(username=search_form['query'].value())
        context['users'] = users
    return render(request, 'main/contacts.html', context)


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
    else:
        user_form = UserRegistrationForm()
    return render(request, 'main/main.html')