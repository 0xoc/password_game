# Generated by Django 2.1.7 on 2019-08-28 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('level', '0004_auto_20190716_1028'),
    ]

    operations = [
        migrations.AddField(
            model_name='level',
            name='hint1farsi',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='level',
            name='hint2farsi',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
