# Generated by Django 5.1.1 on 2024-12-16 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("LittleLemonAPI", "0002_alter_category_title_alter_menuitem_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="date",
            field=models.DateField(auto_created=True, db_index=True),
        ),
    ]
