# Generated by Django 3.0.6 on 2020-05-26 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsApp', '0004_auto_20200523_1425'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='vievs',
            field=models.ImageField(default=0, upload_to=''),
        ),
    ]