# Generated by Django 5.0.7 on 2024-07-16 14:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('imagen', models.ImageField(upload_to='mascotas')),
            ],
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id_mascota', models.AutoField(db_column='idMascota', primary_key=True, serialize=False)),
                ('mascota', models.CharField(max_length=50)),
                ('foto', models.ImageField(upload_to='mascotas')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('rut', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('apellido_paterno', models.CharField(max_length=20)),
                ('apellido_materno', models.CharField(blank=True, max_length=20)),
                ('telefono', models.CharField(max_length=45)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('direccion', models.CharField(max_length=50)),
                ('activo', models.IntegerField()),
                ('id_mascota', models.ForeignKey(db_column='idMascota', on_delete=django.db.models.deletion.PROTECT, to='adopcion.mascota')),
            ],
        ),
    ]
