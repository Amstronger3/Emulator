# Generated by Django 3.2.6 on 2021-08-29 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0011_auto_20210829_2016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='last_update_time',
        ),
        migrations.AlterField(
            model_name='profile',
            name='status_subscrible',
            field=models.CharField(choices=[('SUBSCRIBE', 'subscribe'), ('UNSUBSCRIBE', 'unsubscribe')], default='UNSUBSCRIBE', max_length=15),
        ),
    ]
