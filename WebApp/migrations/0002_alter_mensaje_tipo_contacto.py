# Generated by Django 3.2.7 on 2021-12-02 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensaje',
            name='tipo_contacto',
            field=models.CharField(choices=[('radioterapia', 'RADIOTERAPIA'), ('radiocirujia', 'RADIOCIRUGÍA'), ('braquiterapia', 'BRAQUITERAPIA'), ('fotodinamia', 'FOTODINAMIA'), ('otros', 'OTROS')], max_length=20),
        ),
    ]
