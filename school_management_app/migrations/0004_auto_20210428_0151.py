# Generated by Django 3.2 on 2021-04-27 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_management_app', '0003_auto_20210428_0120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scomment',
            name='created_on',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='tcomment',
            name='created_on',
            field=models.DateField(auto_now_add=True),
        ),
    ]
