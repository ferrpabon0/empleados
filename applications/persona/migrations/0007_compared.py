# Generated by Django 3.0.4 on 2020-04-22 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0006_remove_empleado_habilidades'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compared',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comp', models.CharField(max_length=50, verbose_name='Compared')),
            ],
        ),
    ]