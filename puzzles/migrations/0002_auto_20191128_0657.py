# Generated by Django 2.2.7 on 2019-11-28 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("puzzles", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="puzzle",
            name="channel",
            field=models.CharField(max_length=128, unique=True),
        ),
    ]
