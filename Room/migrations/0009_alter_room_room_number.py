# Generated by Django 3.2 on 2022-05-26 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Room', '0008_rename_desciption_room_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='room_number',
            field=models.IntegerField(unique=True),
        ),
    ]
