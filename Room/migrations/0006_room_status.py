# Generated by Django 3.2 on 2022-05-13 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Room', '0005_auto_20220512_2357'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
