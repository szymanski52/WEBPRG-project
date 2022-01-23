from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.render_main, name='main'),
    path('groups', views.render_main, name='groups'),
    path('settings', views.render_main, name='settings'),
    path('become_researcher', views.render_main, name='become_researcher'),
    path('messages', views.render_messages, name='messages'),
    path('create_group', views.render_main, name='create_group'),
    path('profile', views.render_profile, name='profile'),
    path('register', views.register, name='register'),
    path('auth', views.render_auth, name='auth'),
    path('contacts', views.render_contacts, name='contacts'),
    path('search', views.search, name='search'),
    path('add_contact', views.add_contact, name='add_contact'),
    path('chat/<user_id>', views.render_private_chat, name='chat'),
    path('send_message/<user_id>', views.send_message, name='send_message')
]