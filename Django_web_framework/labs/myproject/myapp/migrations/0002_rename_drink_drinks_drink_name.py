# Generated by Django 5.1.1 on 2024-11-24 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="drinks",
            old_name="drink",
            new_name="drink_name",
        ),
    ]
