# Generated by Django 4.2.18 on 2025-02-03 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reactions', '0004_alter_score_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='hidden',
            field=models.BooleanField(default=False),
        ),
    ]
