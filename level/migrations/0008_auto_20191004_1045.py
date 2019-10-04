# Generated by Django 2.1.7 on 2019-10-04 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('level', '0007_remove_packageuserrelation_passed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='levelpackage',
            name='levels',
        ),
        migrations.AddField(
            model_name='levelpackage',
            name='levels',
            field=models.ManyToManyField(related_name='pack', to='level.Level'),
        ),
    ]
