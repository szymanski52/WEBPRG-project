from django.db import models
from django.contrib.auth.models import User


class Chat(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chat_owner')
    contact = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chat_contact')
    is_private = models.BooleanField(default=True)


class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='message_author')
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='chat_id')
    text = models.CharField(max_length=200, default='Empty message')
    content_dir = models.CharField(max_length=200, null=True)
    date = models.DateTimeField(auto_now_add=True)


class Contact(models.Model):
    user    = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_ID')
    contact = models.ForeignKey(User, on_delete=models.CASCADE, related_name='new_contact_ID')


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rating_user')
    value = models.FloatField(default=0)


class Group(models.Model):
    name = models.CharField(max_length=200, default='Unnamed')


class GroupMember(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='gm_group_id')
    user  = models.ForeignKey(User,  on_delete=models.CASCADE, related_name='gm_user_id')


class UserPicture(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='up_user_id')
    pic = models.CharField(max_length=1000, default='https://bootdey.com/img/Content/avatar/avatar3.png')
