# Generated by Django 4.2 on 2023-05-08 15:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yummy', '0004_alter_mediafile_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='favourites',
            field=models.ManyToManyField(blank=True, default=None, related_name='favourite', to=settings.AUTH_USER_MODEL),
        ),
    ]
