# Generated by Django 3.2.18 on 2023-04-27 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_userprofile_role_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to=('userProfile/profilePic/', models.AutoField(primary_key=True, serialize=False))),
        ),
    ]
