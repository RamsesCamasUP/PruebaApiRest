# Generated by Django 3.1.3 on 2020-11-02 21:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0004_auto_20201102_1511'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='user',
        ),
    ]
