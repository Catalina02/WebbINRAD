# Generated by Django 3.2.7 on 2021-10-18 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0002_auto_20211018_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='img_perfil',
            field=models.ImageField(default='blank-profile-picture-973460_640.png', upload_to='Usuarios'),
        ),
    ]