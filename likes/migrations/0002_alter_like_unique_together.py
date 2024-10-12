# Generated by Django 5.1.1 on 2024-10-12 00:33

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0002_alter_destination_description'),
        ('likes', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='like',
            unique_together={('destination', 'user')},
        ),
    ]