# Generated by Django 3.2.18 on 2023-04-20 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skilltest', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testsessionitems',
            name='question_id',
        ),
    ]
