# Generated by Django 3.2 on 2021-05-26 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_management_app', '0025_auto_20210527_0120'),
    ]

    operations = [
        migrations.RenameField(
            model_name='leavereportstaff',
            old_name='leave_date',
            new_name='leave_start_date',
        ),
        migrations.AddField(
            model_name='leavereportstaff',
            name='leave_end_date',
            field=models.CharField(default='', max_length=255),
        ),
    ]
