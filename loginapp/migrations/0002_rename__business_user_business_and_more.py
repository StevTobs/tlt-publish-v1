# Generated by Django 5.1.1 on 2024-09-04 21:52

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("loginapp", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="_business",
            new_name="business",
        ),
        migrations.RenameField(
            model_name="user",
            old_name="_date",
            new_name="date",
        ),
        migrations.RenameField(
            model_name="user",
            old_name="_email",
            new_name="email",
        ),
        migrations.RenameField(
            model_name="user",
            old_name="_first_name",
            new_name="first_name",
        ),
        migrations.RenameField(
            model_name="user",
            old_name="_last_name",
            new_name="last_name",
        ),
        migrations.RenameField(
            model_name="user",
            old_name="_password",
            new_name="password",
        ),
        migrations.RenameField(
            model_name="user",
            old_name="_province",
            new_name="province",
        ),
        migrations.RenameField(
            model_name="user",
            old_name="_tel",
            new_name="tel",
        ),
        migrations.RenameField(
            model_name="user",
            old_name="_username",
            new_name="username",
        ),
    ]
