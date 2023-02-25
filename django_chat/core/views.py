from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseNotFound, HttpResponse
from django.shortcuts import render
from django_chat.core.forms import AddChatRoomForm, EnterChatRoomForm
from django_chat.core.models import ChatRoom, Message
from django_chat.core.utils import is_room_existing, format_date

UserModel = get_user_model()


def home(request):
    print(ChatRoom.objects.all())
    context = {
        'enter_room_form': EnterChatRoomForm(),
        'add_room_form': AddChatRoomForm(),
        'user': None if str(request.user) == 'AnonymousUser' else request.user,
        'rooms': ChatRoom.objects.all()
    }

    return render(request, 'home.html', context)


@login_required
def add_chat_room(request, room_name):
    add_room_form = AddChatRoomForm(request.POST)
    if add_room_form.is_valid():
        add_room_form.save()
        return JsonResponse(f'Chat room with name {room_name} added successfully!', safe=False)
    return JsonResponse(f'Chat room with name {room_name} already exists.', safe=False)


@login_required
def enter_chat_room(request, room_name):
    if not is_room_existing(room_name, ChatRoom):
        return JsonResponse(f'Chat room with name {room_name} does not exists!', safe=False)
    return JsonResponse('Entering.', safe=False)


@login_required
def chat_room(request, room_name):
    if not is_room_existing(room_name, ChatRoom):
        return HttpResponseNotFound('Room not found!')

    room_id = (ChatRoom.objects.get(room_name=room_name)).id

    context = {
        'room_name': room_name,
        'messages': Message.objects.filter(room_name_id=room_id)
    }

    return render(request, 'chat-room.html', context)


@login_required
def add_message(request, message, sender_id, room_name):
    sender = UserModel.objects.get(id=sender_id)
    room = ChatRoom.objects.get(room_name=room_name)
    Message.objects.create(message=message, sender=sender, room_name=room)
    return HttpResponse()


@login_required
def get_info(request):
    sender = request.user
    date = format_date(str(Message.objects.last().date).split(' '))
    print(Message.objects.last().date)
    return JsonResponse(f'{sender}|{date}', safe=False)
