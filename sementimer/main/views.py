from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegistrationForm, SearchForm, AddContactForm
from .models import Contact
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
    contacts_ids = Contact.objects.filter(user=request.user)
    contacts = User.objects.filter(id__in=contacts_ids)
    context['contacts'] = contacts
    return render(request, 'main/messages.html', context)


def render_contacts(request):
    context = {}
    contacts_ids = Contact.objects.filter(user=request.user)
    contacts = User.objects.filter(id__in=contacts_ids)
    context['contacts'] = contacts
    return render(request, 'main/contacts.html', context)


def search(request):
    context = {}
    if request.method == 'POST':
        search_form = SearchForm(request.POST)
        users = User.objects.filter(username=search_form['query'].value())
        context['users'] = users
    return render(request, 'main/contacts.html', context)


def add_contact(request):
    if request.method == 'POST':
        add_contact_form = AddContactForm(request.POST)
        user = User.objects.get(id=add_contact_form.data['contact_id'][0])
        print(user)
        new_contact = Contact(user=request.user, contact=user)
        new_contact.save()
    return redirect('contacts')


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