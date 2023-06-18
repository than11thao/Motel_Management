# Generated by Django 3.2 on 2022-05-13 01:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Room', '0006_room_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Room.room')),
            ],
        ),
    ]
