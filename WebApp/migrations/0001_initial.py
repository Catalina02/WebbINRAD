# Generated by Django 3.2.7 on 2021-11-29 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('correo_contacto', models.EmailField(max_length=254)),
                ('tipo_contacto', models.IntegerField(choices=[[0, 'RADIOTERAPIA'], [1, 'RADIOCIRUGÍA'], [2, 'BRAQUITERAPIA'], [3, 'FOTODINAMIA'], [4, 'OTROS']])),
                ('mensaje', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Correo Electronico')),
                ('nombre', models.CharField(max_length=255, verbose_name='Nombre')),
                ('apellido_paterno', models.CharField(max_length=255, verbose_name='Apellido Paterno')),
                ('apellido_materno', models.CharField(max_length=255, verbose_name='Apellido Materno')),
                ('rut', models.IntegerField(unique=True)),
                ('dv', models.CharField(max_length=1)),
                ('foto_perfil', models.ImageField(default='blank-profile-picture-973460_640.png', null=True, upload_to='Usuarios/', verbose_name='Foto de Perfil')),
                ('usuario_activo', models.BooleanField(default=True)),
                ('usuario_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
