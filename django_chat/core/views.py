from django.http import JsonResponse
from django.shortcuts import render, redirect
from django_chat.core.forms import AddChatRoomForm, EnterChatRoomForm


def home(request):
    if request.method == 'GET':
        enter_room_form = EnterChatRoomForm()
    else:
        enter_room_form = EnterChatRoomForm(request.POST)
        if enter_room_form.is_valid():
            enter_room_form.save()
            return redirect('chat room', room_name=request.POST.get('room_name'))

    context = {
        'enter_room_form': enter_room_form,
        'add_room_form': AddChatRoomForm()
    }

    return render(request, 'home.html', context)


def add_chat_room(request, room_name):
    add_room_form = AddChatRoomForm(request.POST)
    if add_room_form.is_valid():
        add_room_form.save()
        return JsonResponse(f'Chat room with name {room_name} added successfully!', safe=False)
    return JsonResponse(f'Chat room with name {room_name} already exists.', safe=False)


def chat_room(request, room_name):
    return render(request, 'chat-room.html', {'room_name': room_name})
