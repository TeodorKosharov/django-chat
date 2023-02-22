from datetime import datetime
from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class ChatRoom(models.Model):
    room_name = models.CharField(max_length=10, null=False, blank=False, unique=True)


class Message(models.Model):
    sender = models.ForeignKey(UserModel, on_delete=models.CASCADE, unique=False)
    message = models.CharField(max_length=300, null=False, blank=False)
    room_name = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, unique=False)
    date = models.DateTimeField(default=datetime.now())
