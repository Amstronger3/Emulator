# Generated by Django 3.2.6 on 2021-08-30 08:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0019_alter_profile_last_update_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='last_update_time',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
