# Generated by Django 4.1.5 on 2023-02-22 20:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_chatroom_room_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 22, 22, 32, 34, 950117)),
        ),
    ]
