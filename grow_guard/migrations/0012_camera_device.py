# Generated by Django 4.2.7 on 2023-12-13 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grow_guard', '0011_remove_camera_device'),
    ]

    operations = [
        migrations.AddField(
            model_name='camera',
            name='device',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='grow_guard.device'),
        ),
    ]