# Generated by Django 3.2 on 2022-05-31 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bill', '0006_alter_bill_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='discount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='bill',
            name='electricity_price',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bill',
            name='water_price',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='BillDetail',
        ),
    ]
