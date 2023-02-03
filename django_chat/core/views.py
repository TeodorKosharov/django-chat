from django.shortcuts import render, redirect
from django_chat.core.forms import AddChatRoomForm, EnterChatRoomForm


def home(request):
    if request.method == 'GET':
        form = EnterChatRoomForm()
    else:
        form = EnterChatRoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('chat room', room_name=request.POST.get('room_name'))

    return render(request, 'home.html', {'form': form})


def chat_room(request, room_name):
    return render(request, 'chat-room.html', {'room_name': room_name})
