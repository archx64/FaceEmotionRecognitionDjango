# Generated by Django 3.1.5 on 2021-01-24 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_auto_20210124_0843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='time',
            field=models.TextField(default='0', max_length=50),
        ),
    ]
