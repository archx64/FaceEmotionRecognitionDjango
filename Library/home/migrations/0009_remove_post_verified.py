# Generated by Django 3.1.5 on 2021-01-19 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20210120_0126'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='verified',
        ),
    ]
