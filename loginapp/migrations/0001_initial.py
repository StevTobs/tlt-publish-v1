# Generated by Django 5.1.1 on 2024-09-04 19:49

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("_username", models.CharField(max_length=100)),
                ("_password", models.CharField(max_length=100)),
                ("_first_name", models.CharField(max_length=100)),
                ("_last_name", models.CharField(max_length=100)),
                ("_tel", models.CharField(max_length=100)),
                ("_province", models.CharField(max_length=100)),
                ("_business", models.CharField(max_length=100)),
                ("_email", models.CharField(max_length=100)),
                ("_date", models.DateField(auto_now_add=True)),
            ],
        ),
    ]
