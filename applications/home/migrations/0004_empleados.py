# Generated by Django 3.0.3 on 2020-04-01 20:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20200401_1931'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleados',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='home.Persona')),
                ('empleo', models.CharField(max_length=50, verbose_name='Empleo')),
            ],
            bases=('home.persona',),
        ),
    ]
