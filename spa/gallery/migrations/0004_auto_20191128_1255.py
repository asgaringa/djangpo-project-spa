# Generated by Django 2.2.5 on 2019-11-28 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_auto_20191128_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='image',
            field=models.ImageField(blank=True, upload_to='gallery/'),
        ),
    ]
