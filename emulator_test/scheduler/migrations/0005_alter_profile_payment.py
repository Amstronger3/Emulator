# Generated by Django 3.2.6 on 2021-08-29 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0004_alter_profile_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='payment',
            field=models.CharField(choices=[('PAID', 'paid'), ('UNPAID', 'unpaid')], default=('UNPAID', 'unpaid'), max_length=10),
        ),
    ]
