# Generated by Django 5.1.1 on 2024-10-12 00:33

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]