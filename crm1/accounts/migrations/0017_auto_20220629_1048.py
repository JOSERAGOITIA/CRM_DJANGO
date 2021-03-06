# Generated by Django 2.2.3 on 2022-06-29 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_auto_20220629_0215'),
    ]

    operations = [
        migrations.CreateModel(
            name='type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, choices=[('MENTOR', 'Mentor'), ('MEMBER', 'Member')], default=None, max_length=20, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='customer',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.type'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Aproved', 'Aproved')], max_length=200, null=True),
        ),
    ]
