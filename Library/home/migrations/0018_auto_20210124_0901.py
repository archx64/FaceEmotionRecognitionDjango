# Generated by Django 3.1.5 on 2021-01-24 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_auto_20210124_0853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='time',
            field=models.TextField(default='0000', max_length=50),
        ),
    ]
