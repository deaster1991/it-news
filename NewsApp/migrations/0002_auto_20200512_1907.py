# Generated by Django 3.0.6 on 2020-05-12 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Название новости'),
        ),
    ]