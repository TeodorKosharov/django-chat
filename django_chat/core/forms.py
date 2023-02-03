from django import forms
from django_chat.core.models import ChatRoom


class AddChatRoomForm(forms.ModelForm):
    class Meta:
        model = ChatRoom
        fields = '__all__'


class EnterChatRoomForm(forms.ModelForm):
    class Meta:
        model = ChatRoom
        fields = '__all__'
