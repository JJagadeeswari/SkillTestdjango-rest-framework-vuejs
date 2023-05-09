# Generated by Django 4.2 on 2023-04-29 05:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("quesapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Type",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("type", models.CharField(max_length=200, unique=True)),
                ("is_active", models.BooleanField(default=True)),
                ("is_delete", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "db_table": "Type",
            },
        ),
    ]