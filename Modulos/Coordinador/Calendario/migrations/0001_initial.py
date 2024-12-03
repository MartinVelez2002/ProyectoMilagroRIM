# Generated by Django 5.1.2 on 2024-11-23 15:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Turno', '0001_initial'),
        ('Ubicacion', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Calendario_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('estado', models.BooleanField(default=True)),
            ],
            options={
                'constraints': [models.UniqueConstraint(fields=('fecha_inicio', 'fecha_fin'), name='fecha_unica')],
            },
        ),
        migrations.CreateModel(
            name='TurnUsuario_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('calendario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Calendario.calendario_model')),
                ('turno', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Turno.turno_model')),
                ('ubicacion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Ubicacion.ubicacion_model')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
