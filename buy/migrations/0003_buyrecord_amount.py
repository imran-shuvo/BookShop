# Generated by Django 2.2 on 2019-09-06 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buy', '0002_auto_20190906_0240'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyrecord',
            name='amount',
            field=models.IntegerField(default=1),
        ),
    ]
