# Generated by Django 3.0.4 on 2020-04-26 02:19

from django.db import migrations
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0012_auto_20200422_1239'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='hoja_vida',
            field=django_ckeditor_5.fields.CKEditor5Field(default='texto', verbose_name='Text'),
            preserve_default=False,
        ),
    ]
