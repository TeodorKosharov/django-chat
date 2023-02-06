from django.http import JsonResponse, HttpResponseNotFound
from django.shortcuts import render
from django_chat.core.forms import AddChatRoomForm, EnterChatRoomForm
from django_chat.core.models import ChatRoom
from django_chat.core.utils import is_room_existing


def home(request):
    context = {
        'enter_room_form': EnterChatRoomForm(),
        'add_room_form': AddChatRoomForm()
    }

    return render(request, 'home.html', context)


def add_chat_room(request, room_name):
    add_room_form = AddChatRoomForm(request.POST)
    if add_room_form.is_valid():
        add_room_form.save()
        return JsonResponse(f'Chat room with name {room_name} added successfully!', safe=False)
    return JsonResponse(f'Chat room with name {room_name} already exists.', safe=False)


def enter_chat_room(request, room_name):
    if not is_room_existing(room_name, ChatRoom):
        return JsonResponse(f'Chat room with name {room_name} does not exists!', safe=False)
    return JsonResponse('Entering.', safe=False)


def chat_room(request, room_name):
    if not is_room_existing(room_name, ChatRoom):
        return HttpResponseNotFound('Room not found!')

    return render(request, 'chat-room.html', {'room_name': room_name})
