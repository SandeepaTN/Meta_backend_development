# Generated by Django 5.1.1 on 2024-12-08 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("MenuAPI", "0004_menu_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="menu",
            name="price",
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
