# Generated by Django 5.0.7 on 2024-07-16 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adopcion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='edad',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
