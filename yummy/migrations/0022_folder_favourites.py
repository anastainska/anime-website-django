# Generated by Django 4.2 on 2023-05-11 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yummy', '0021_remove_user_user_id_idx'),
    ]

    operations = [
        migrations.AddField(
            model_name='folder',
            name='favourites',
            field=models.ManyToManyField(related_name='favorited_by', to='yummy.anime'),
        ),
    ]
