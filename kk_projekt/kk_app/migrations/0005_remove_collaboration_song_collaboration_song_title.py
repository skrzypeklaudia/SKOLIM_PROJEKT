# Generated by Django 5.1.4 on 2025-01-24 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kk_app', '0004_rename_colaboration_collaboration_collaboration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collaboration',
            name='song',
        ),
        migrations.AddField(
            model_name='collaboration',
            name='song_title',
            field=models.CharField(default='', help_text='Tytuł piosenki Skolima', max_length=100),
            preserve_default=False,
        ),
    ]
