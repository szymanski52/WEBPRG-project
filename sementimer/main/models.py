from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='message_author')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='message_recipient')
    text = models.CharField(max_length=200, default='Empty message')
    content_dir = models.CharField(max_length=200, null=True)


class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_ID')
    contact = models.ForeignKey(User, on_delete=models.CASCADE, related_name='new_contact_ID')
