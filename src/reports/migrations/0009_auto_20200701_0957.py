# Generated by Django 3.0.7 on 2020-07-01 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0008_auto_20200701_0954'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dailyreport',
            name='discipline',
        ),
        migrations.RemoveField(
            model_name='dailyreport',
            name='pgesco_id',
        ),
        migrations.RemoveField(
            model_name='dailyreport',
            name='title',
        ),
    ]
