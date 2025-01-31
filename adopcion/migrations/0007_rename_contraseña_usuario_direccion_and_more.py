# Generated by Django 5.0.7 on 2024-07-17 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adopcion', '0006_remove_usuario_id_usuario_usuario_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='contraseña',
            new_name='direccion',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='id',
        ),
        migrations.AddField(
            model_name='usuario',
            name='activo',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='apellido_materno',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='usuario',
            name='apellido_paterno',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='rut',
            field=models.CharField(default=1, max_length=10, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='telefono',
            field=models.CharField(default=1, max_length=45),
            preserve_default=False,
        ),
    ]
