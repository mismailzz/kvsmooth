# Generated by Django 2.2 on 2022-07-28 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0002_auto_20220728_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hypervisortabledb',
            name='ipAddress',
            field=models.CharField(blank=True, default='', max_length=16, null=True),
        ),
    ]
