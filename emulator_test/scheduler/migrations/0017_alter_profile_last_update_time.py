# Generated by Django 3.2.6 on 2021-08-29 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0016_alter_profile_last_update_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='last_update_time',
            field=models.DateTimeField(null=True),
        ),
    ]