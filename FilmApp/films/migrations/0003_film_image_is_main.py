# Generated by Django 3.0.3 on 2020-02-21 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0002_auto_20200221_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='film_image',
            name='is_main',
            field=models.BooleanField(default=False),
        ),
    ]