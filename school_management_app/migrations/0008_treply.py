# Generated by Django 3.2 on 2021-04-27 19:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school_management_app', '0007_alter_tcomment_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='TReply',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('body', models.TextField()),
                ('created_on', models.DateField(auto_now_add=True)),
                ('count', models.IntegerField(default='1')),
                ('TComment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='school_management_app.tcomment')),
                ('staff_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
