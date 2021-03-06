# Generated by Django 3.0.3 on 2020-03-26 02:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('libros', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lectores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellidos', models.CharField(max_length=30)),
                ('nacionalidad', models.CharField(max_length=20)),
                ('edad', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='prestamos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_prestame', models.DateField()),
                ('fecha_devolucion', models.DateField(blank=True, null=True)),
                ('devuelto', models.BooleanField()),
                ('lector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lectores.Lectores')),
                ('libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libros.Libros')),
            ],
        ),
    ]
