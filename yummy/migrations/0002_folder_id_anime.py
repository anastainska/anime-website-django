# Generated by Django 4.2 on 2023-05-04 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yummy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='folder',
            name='id_anime',
            field=models.ManyToManyField(to='yummy.anime'),
        ),
    ]
