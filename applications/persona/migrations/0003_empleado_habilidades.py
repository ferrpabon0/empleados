# Generated by Django 3.0.4 on 2020-04-19 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0002_auto_20200419_1024'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='habilidades',
            field=models.ManyToManyField(to='persona.Habilidades'),
        ),
    ]