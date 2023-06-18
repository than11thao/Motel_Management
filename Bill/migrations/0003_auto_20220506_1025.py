# Generated by Django 3.2.1 on 2022-05-06 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bill', '0002_billdetail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bill',
            name='total_amount',
        ),
        migrations.AddField(
            model_name='bill',
            name='room_fee',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]