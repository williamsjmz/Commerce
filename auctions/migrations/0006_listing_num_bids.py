# Generated by Django 3.1.7 on 2021-06-02 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_auto_20210602_1741'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='num_bids',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
