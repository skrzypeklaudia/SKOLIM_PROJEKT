# Generated by Django 5.1.4 on 2025-01-24 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kk_app', '0005_remove_collaboration_song_collaboration_song_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collaboration',
            name='song_title',
            field=models.CharField(default='', help_text='Tytuł piosenki Skolima', max_length=100),
        ),
    ]
