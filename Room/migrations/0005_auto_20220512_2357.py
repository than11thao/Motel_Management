# Generated by Django 3.2 on 2022-05-12 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Room', '0004_room_s'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='room',
            name='s',
        ),
        migrations.AddConstraint(
            model_name='room',
            constraint=models.CheckConstraint(check=models.Q(('area__gte', 0), ('room_number__gte', 0), ('room_price__gte', 0)), name='gte 0'),
        ),
    ]