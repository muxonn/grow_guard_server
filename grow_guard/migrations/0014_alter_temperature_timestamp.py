# Generated by Django 4.2.7 on 2023-12-18 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grow_guard', '0013_temperature_lighting_humidity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temperature',
            name='timestamp',
            field=models.DateTimeField(),
        ),
    ]