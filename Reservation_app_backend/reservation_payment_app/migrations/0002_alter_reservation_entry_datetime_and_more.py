# Generated by Django 5.0.3 on 2024-05-13 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation_payment_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='entry_datetime',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='exit_datetime',
            field=models.CharField(max_length=50),
        ),
    ]
