# Generated by Django 3.0.3 on 2020-04-03 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autores', '0002_auto_20200401_2039'),
    ]

    operations = [
        migrations.AddField(
            model_name='autores',
            name='suedonimo',
            field=models.CharField(blank=True, max_length=50, verbose_name='Seudonomio'),
        ),
    ]