# Generated by Django 2.2.5 on 2019-11-28 05:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_auto_20191128_1255'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gallery',
            old_name='image',
            new_name='cover',
        ),
    ]
