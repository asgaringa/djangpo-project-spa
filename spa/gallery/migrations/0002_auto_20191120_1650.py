# Generated by Django 2.2.5 on 2019-11-20 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Gallery',
            new_name='Image',
        ),
    ]
