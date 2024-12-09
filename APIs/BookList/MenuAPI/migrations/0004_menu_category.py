# Generated by Django 5.1.1 on 2024-12-05 10:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("MenuAPI", "0003_remove_menu_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="menu",
            name="category",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                to="MenuAPI.category",
            ),
            preserve_default=False,
        ),
    ]
