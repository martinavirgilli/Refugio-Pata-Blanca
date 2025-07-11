# Generated by Django 5.2.4 on 2025-07-08 00:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('tipo', models.CharField(max_length=50)),
                ('raza', models.CharField(max_length=100)),
                ('edad', models.PositiveIntegerField()),
                ('descripcion', models.TextField()),
                ('estado', models.CharField(default='disponible', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='FormularioAdopcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_solicitud', models.DateField(auto_now_add=True)),
                ('estado', models.CharField(default='pendiente', max_length=20)),
                ('comentarios', models.TextField(blank=True)),
                ('candidato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='formularios', to='api.candidato')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='formularios', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Visita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_visita', models.DateField()),
                ('observaciones', models.TextField(blank=True)),
                ('formulario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='visita', to='api.formularioadopcion')),
            ],
        ),
    ]
