# Generated by Django 3.0.3 on 2020-04-01 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20200401_1927'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='persona',
            unique_together={('pais', 'apelativo')},
        ),
        migrations.AddConstraint(
            model_name='persona',
            constraint=models.CheckConstraint(check=models.Q(edad__gte=18), name='edad_mayor_18'),
        ),
    ]