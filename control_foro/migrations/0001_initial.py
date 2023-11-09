# Generated by Django 4.2.6 on 2023-11-07 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CrearForo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_foro', models.CharField(max_length=64, verbose_name='Nombre del Foro')),
                ('tema_foro', models.CharField(choices=[('Comida', 'Comida'), ('Salud', 'Salud'), ('Ejercio', 'Ejercicio'), ('Otro', 'Otro')], max_length=7)),
                ('contenido_foro', models.CharField(max_length=1500, verbose_name='Contenido del Foro')),
            ],
        ),
        migrations.CreateModel(
            name='Forista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apellido', models.CharField(max_length=256)),
                ('nombre', models.CharField(max_length=256)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('dni', models.CharField(max_length=32)),
                ('fecha_nacimiento', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RespuestaForo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('respuesta_Foro', models.CharField(max_length=1500, verbose_name='Contenido del Foro')),
            ],
        ),
    ]