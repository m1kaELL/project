# Generated by Django 3.0.3 on 2020-02-22 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0004_auto_20200222_1102'),
    ]

    operations = [
        migrations.AddField(
            model_name='film_genre',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
