# Generated by Django 3.2 on 2022-05-12 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Room', '0002_alter_room_capacity'),
        ('User', '0005_auto_20220512_2229'),
    ]

    operations = [
        migrations.CreateModel(
            name='Renter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('citizen_id', models.CharField(max_length=15, null=True)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='renter', to='Room.room')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='User.myuser')),
            ],
        ),
    ]
