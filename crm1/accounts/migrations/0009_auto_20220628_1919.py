# Generated by Django 2.2.3 on 2022-06-29 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_remove_customer_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='employer',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='location',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
