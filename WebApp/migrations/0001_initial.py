# Generated by Django 3.2.7 on 2021-10-18 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido_paterno', models.CharField(max_length=100)),
                ('apellido_materno', models.CharField(max_length=100)),
                ('rut', models.IntegerField()),
                ('dv', models.IntegerField()),
                ('fecha_nacimiento', models.DateTimeField()),
            ],
        ),
    ]
