# Generated by Django 3.0.3 on 2020-04-01 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50, verbose_name='Nombres')),
                ('pais', models.CharField(max_length=50, verbose_name='Pais')),
                ('pasaporte', models.CharField(max_length=50, verbose_name='Pasaporte')),
                ('edad', models.IntegerField()),
                ('apelativo', models.CharField(max_length=10, verbose_name='Legajo')),
            ],
            options={
                'verbose_name': 'Persona',
                'verbose_name_plural': 'Personas',
                'db_table': 'Personas',
            },
        ),
    ]