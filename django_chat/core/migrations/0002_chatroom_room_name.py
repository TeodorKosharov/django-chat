# Generated by Django 4.1.5 on 2023-02-02 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatroom',
            name='room_name',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]