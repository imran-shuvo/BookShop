# Generated by Django 2.2 on 2019-09-06 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyrecord',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='buytotal',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]