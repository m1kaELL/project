# Generated by Django 3.0.3 on 2020-02-21 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='short_description',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='film_image',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='Subscribers/static/media/films_images/'),
        ),
    ]
