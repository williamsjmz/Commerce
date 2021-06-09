# Generated by Django 3.1.7 on 2021-05-31 22:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_auto_20210528_1911'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='comment',
        ),
        migrations.AddField(
            model_name='comment',
            name='listing',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users_comments', to='auctions.listing'),
        ),
    ]
