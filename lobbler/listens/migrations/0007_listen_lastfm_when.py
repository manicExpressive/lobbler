# Generated by Django 5.0.6 on 2024-05-28 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listens', '0006_alter_listen_when'),
    ]

    operations = [
        migrations.AddField(
            model_name='listen',
            name='lastfm_when',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
