# Generated by Django 3.2 on 2022-06-09 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Feed_Back', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]