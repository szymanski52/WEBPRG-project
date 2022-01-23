from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, AnonymousUser
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegistrationForm, SearchForm, AddContactForm
from .models import Contact, Message, Chat, Rating, UserPicture
import random
import os


def render_main(request):
    return render(request, 'main/main.html')


def render_auth(request):
    context = {'user_form': UserRegistrationForm(), 'form': AuthenticationForm()}
    return render(request, 'main/auth.html', context)


def render_profile(request):
    if not request.user.is_authenticated:
        return redirect('auth')
    context = {}
    img = UserPicture.objects.filter(user=request.user)
    rating = Rating.objects.filter(user=request.user)
    try:
        context['rating'] = round(rating[0].value, 2)
    except:
        context['rating'] = 0.54
    if len(img):
        context['pic'] = img[0].pic
    return render(request, 'main/profile.html', context)


def render_messages(request):
    if not request.user.is_authenticated:
        return redirect('auth')
    context = {}
    contacts = Contact.objects.filter(user=request.user)
    #contacts = User.objects.filter(id__in=contacts_ids)
    contacts_ids = [i.contact.id for i in contacts]
    contacts_users = User.objects.filter(id__in=contacts_ids)
    context['contacts'] = contacts_users
    return render(request, 'main/messages.html', context)


def render_contacts(request):
    if not request.user.is_authenticated:
        return redirect('auth')
    context = {}
    contacts = Contact.objects.filter(user=request.user)
    contacts_ids = [i.contact.id for i in contacts]
    contacts_users = User.objects.filter(id__in=contacts_ids)
    contacts_dir = {}
    for i in contacts_users:
        img = UserPicture.objects.filter(user=i)
        rating = Rating.objects.filter(user=i)
        try:
            rating = round(rating[0].value, 2)
        except:
            rating = 0.54
        contacts_dir[i.id] = {'contact': i, 'pic': img, 'rating': rating}
    context['contacts'] = contacts_dir
    return render(request, 'main/contacts.html', context)


def send_message(request, user_id):
    if not request.user.is_authenticated:
        return redirect('auth')
    context = {}
    if request.method == 'POST':
        contact = User.objects.get(id=user_id)
        chat = Chat.objects.filter(Q(owner=request.user, contact=contact) |
                                   Q(owner=contact, contact=request.user))[0]
        new_message = Message(author=request.user,
                              chat=chat,
                              text=request.POST['msg-text'])
        new_message.save()
        new_message = Message()
    return HttpResponseRedirect(f'/chat/{user_id}')


def render_private_chat(request, user_id):
    if not request.user.is_authenticated:
        return redirect('auth')
    context = {}
    classes = ['chat-message-left', 'chat-message-right']
    messages_dir = {}
    contacts_dir = {}
    contact = User.objects.get(id=user_id)
    context['contact'] = contact
    contacts = Contact.objects.filter(user=request.user)
    contacts_ids = [i.contact.id for i in contacts]
    contacts_users = User.objects.filter(id__in=contacts_ids)
    for i in contacts_users:
        img = UserPicture.objects.filter(user=i)
        if len(img):
            img = img[0]
        contacts_dir[i.id] = {'contact': i, 'pic': img.pic}
    context['contacts'] = contacts_dir
    contact_pic = UserPicture.objects.filter(user=contact)
    if len(contact_pic):
        contact_pic = contact_pic[0].pic
    context['contact_pic'] = contact_pic
    print(contacts_dir)
    try:
        chat = Chat.objects.filter(Q(owner=request.user, contact=contact) |
                                   Q(owner=contact, contact=request.user))
        messages = Message.objects.filter(chat=chat[0]).order_by('-date')[:100]
        for i in messages:
            if i.author == request.user:
                img = UserPicture.objects.filter(user=request.user)
                if len(img):
                    img = img[0].pic
            else:
                img = UserPicture.objects.filter(user=i.author)
                if len(img):
                    img = img[0].pic
            messages_dir[i.id] = {'text': i.text, 'class': classes[i.author == request.user], 'pic': img}
        context['messages'] = messages_dir
        print(messages_dir)
    except:
        chat = Chat(owner=request.user, contact=contact)
        chat.save()
    context['recipient'] = user_id
    return render(request, 'main/chat.html', context)


def search(request):
    context = {}
    if request.method == 'POST':
        search_form = SearchForm(request.POST)
        users = User.objects.filter(username=search_form.data['query'])
        context['users'] = users
    return render(request, 'main/contacts.html', context)


def add_contact(request):
    if not request.user.is_authenticated:
        return redirect('auth')
    if request.method == 'POST':
        add_contact_form = AddContactForm(request.POST)
        user = User.objects.get(id=add_contact_form.data['contact_id'][0])
        new_contact = Contact(user=request.user, contact=user)
        new_contact.save()
        vv_contact = Contact(user=user, contact=request.user)
        vv_contact.save()
    return redirect('contacts')


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            rating = Rating(user=new_user, value=random.uniform(0.01, 14.88))
            rating.save()
            pic_index = random.randrange(1, 10)
            user_pic = UserPicture(user=new_user, pic=f"https://bootdey.com/img/Content/avatar/avatar{pic_index}.png")
            user_pic.save()
    else:
        user_form = UserRegistrationForm()
    return render(request, 'main/main.html')