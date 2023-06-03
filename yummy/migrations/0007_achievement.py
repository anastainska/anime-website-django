# Generated by Django 4.2 on 2023-05-09 21:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yummy', '0006_remove_anime_favourites_folder_favourites'),
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('timecode', models.TimeField()),
                ('media_file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yummy.mediafile')),
            ],
        ),
    ]
