# Generated by Django 3.0.3 on 2020-03-28 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0003_auto_20200327_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libros',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categoria_libro', to='libros.Categorias'),
        ),
    ]
