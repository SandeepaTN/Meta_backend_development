# Generated by Django 5.1.1 on 2024-11-28 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("demoapp", "0013_alter_application_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="application",
            name="resume",
            field=models.FileField(upload_to="resume"),
        ),
    ]