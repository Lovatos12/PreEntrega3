# Generated by Django 4.2.6 on 2023-11-09 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control_foro', '0002_rename_contenido_foro_crearforo_contenido_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='forista',
            name='sexo',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino'), ('D', 'Default')], default='D', max_length=1),
        ),
    ]
