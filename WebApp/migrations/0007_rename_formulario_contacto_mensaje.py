# Generated by Django 3.2.7 on 2021-10-26 03:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0006_remove_formulario_contacto_avisos'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Formulario_Contacto',
            new_name='Mensaje',
        ),
    ]