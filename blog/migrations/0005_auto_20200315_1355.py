# Generated by Django 3.0.4 on 2020-03-15 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200315_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pic',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
