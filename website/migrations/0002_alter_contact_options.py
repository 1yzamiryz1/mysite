# Generated by Django 4.2.7 on 2023-12-17 14:04

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="contact",
            options={"ordering": ("created_date",)},
        ),
    ]