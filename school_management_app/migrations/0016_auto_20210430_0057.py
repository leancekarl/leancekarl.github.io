# Generated by Django 3.2 on 2021-04-29 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_management_app', '0015_auto_20210429_2346'),
    ]

    operations = [
        migrations.AddField(
            model_name='adminhod',
            name='profile_pic',
            field=models.FileField(default='', upload_to=''),
        ),
        migrations.AddField(
            model_name='staffs',
            name='profile_pic',
            field=models.FileField(default='', upload_to=''),
        ),
    ]
