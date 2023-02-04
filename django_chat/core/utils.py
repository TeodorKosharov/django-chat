def is_room_existing(room_name, chat_room):
    return room_name in [room.room_name for room in chat_room.objects.all()]
