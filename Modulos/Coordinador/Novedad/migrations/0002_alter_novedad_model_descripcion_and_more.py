# Generated by Django 5.1.2 on 2024-11-26 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Novedad', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='novedad_model',
            name='descripcion',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='tiponovedad_model',
            name='descripcion',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='novedad_model',
            unique_together={('descripcion', 'tiponovedad')},
        ),
    ]