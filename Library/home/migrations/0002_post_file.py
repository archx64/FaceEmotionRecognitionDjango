# Generated by Django 3.0.7 on 2020-07-09 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='file',
            field=models.FileField(default='dummy.pdf', upload_to='pdf_files'),
        ),
    ]