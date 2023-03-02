from django import forms
from django_chat.core.models import ChatRoom


class AddChatRoomForm(forms.ModelForm):
    class Meta:
        model = ChatRoom
        fields = ('room_name',)
        labels = {
            'room_name': ''
        }
        widgets = {
            'room_name': forms.TextInput(attrs={
                'placeholder': 'Create chat room',
                'class': 'room-form-input'
            }),
        }


class EnterChatRoomForm(forms.ModelForm):
    class Meta:
        model = ChatRoom
        fields = ('room_name',)
        labels = {
            'room_name': ''
        }
        widgets = {
            'room_name': forms.TextInput(attrs={
                'placeholder': 'Enter chat room',
                'class': 'room-form-input'
            })
        }
