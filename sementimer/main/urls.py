from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.render_main, name='main'),
    path('groups', views.render_main, name='groups'),
    path('settings', views.render_main, name='settings'),
    path('become_researcher', views.render_main, name='become_researcher'),
    path('messages', views.render_main, name='messages'),
    path('create_group', views.render_main, name='create_group'),
    path('profile', views.render_main, name='profile'),
]