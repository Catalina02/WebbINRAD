# Generated by Django 3.2.7 on 2021-12-06 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0003_alter_usuario_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='fecha_de_alta',
            field=models.DateField(null=True, verbose_name='Fecha Ingreso al Sistema'),
        ),
    ]