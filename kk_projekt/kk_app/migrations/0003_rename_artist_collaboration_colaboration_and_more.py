# Generated by Django 5.1.4 on 2025-01-24 20:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kk_app', '0002_alter_album_release_date_alter_song_release_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='collaboration',
            old_name='artist',
            new_name='colaboration',
        ),
        migrations.AlterField(
            model_name='collaboration',
            name='song',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kk_app.song'),
        ),
        migrations.AlterField(
            model_name='song',
            name='duration',
            field=models.DurationField(help_text='Czas trwania piosenki (HH:MM:SS)'),
        ),
        migrations.AlterField(
            model_name='song',
            name='release_date',
            field=models.DateField(help_text='Data wydania piosenki'),
        ),
    ]
