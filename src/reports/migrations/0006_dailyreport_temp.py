# Generated by Django 3.0.7 on 2020-07-01 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0005_auto_20200701_0811'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailyreport',
            name='temp',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
