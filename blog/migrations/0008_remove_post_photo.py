# Generated by Django 3.0.4 on 2020-03-15 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200315_1358'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='photo',
        ),
    ]