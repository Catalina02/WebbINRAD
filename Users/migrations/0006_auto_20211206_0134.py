# Generated by Django 3.2.7 on 2021-12-06 04:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0005_auto_20211206_0116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='username',
        ),
    ]
