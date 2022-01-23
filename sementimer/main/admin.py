from django.contrib import admin
from .models import Contact, Chat, Message, Rating, Group, GroupMember, UserPicture

admin.site.register(Contact)
admin.site.register(Chat)
admin.site.register(Message)
admin.site.register(Rating)
admin.site.register(Group)
admin.site.register(GroupMember)
admin.site.register(UserPicture)

# Register your models here.
