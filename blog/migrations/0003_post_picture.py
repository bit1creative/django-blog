# Generated by Django 3.0.4 on 2020-03-15 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='picture',
            field=models.ImageField(default=None, upload_to=''),
            preserve_default=False,
        ),
    ]
