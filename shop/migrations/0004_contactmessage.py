# Generated by Django 5.1.2 on 2024-10-19 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0003_rename_ordered_at_order_ordered_date_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="ContactMessage",
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
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("message", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
