# Generated by Django 2.2.3 on 2022-06-29 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0022_auto_20220629_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('MentorPending', 'MentorPendign'), ('MentorAproved', 'MentorAproved'), ('MemberPending', 'MemberAproved'), ('MemberAproved', 'MemberAproved')], max_length=200, null=True),
        ),
    ]
