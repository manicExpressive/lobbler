# Generated by Django 5.0.6 on 2024-05-28 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listens', '0003_alter_song_release'),
    ]

    operations = [
        migrations.AddField(
            model_name='listen',
            name='json_from_source',
            field=models.TextField(blank=True, null=True),
        ),
    ]