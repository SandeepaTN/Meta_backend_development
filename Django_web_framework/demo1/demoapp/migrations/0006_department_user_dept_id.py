# Generated by Django 5.1.1 on 2024-11-24 08:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("demoapp", "0005_rename_use_user"),
    ]

    operations = [
        migrations.CreateModel(
            name="Department",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Department_name", models.CharField(max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name="user",
            name="dept_id",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.PROTECT,
                to="demoapp.department",
            ),
        ),
    ]
