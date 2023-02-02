from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Message(models.Model):
    sender = models.ForeignKey(UserModel, on_delete=models.CASCADE, unique=False)
    message = models.CharField(max_length=300, null=False, blank=False)


class ChatRoom(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE, unique=False)
