# Generated by Django 4.2 on 2023-04-18 16:14

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="bookmark",
            name="book",
        ),
        migrations.RemoveField(
            model_name="bookmark",
            name="marker",
        ),
    ]
