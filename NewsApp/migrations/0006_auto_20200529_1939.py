# Generated by Django 3.0.6 on 2020-05-29 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NewsApp', '0005_news_vievs'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='vievs',
            new_name='views',
        ),
    ]