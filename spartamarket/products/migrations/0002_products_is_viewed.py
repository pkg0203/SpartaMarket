# Generated by Django 4.2 on 2024-04-17 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='is_viewed',
            field=models.IntegerField(default=0),
        ),
    ]
