# Generated by Django 2.2.3 on 2022-06-29 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0021_remove_order_product'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
