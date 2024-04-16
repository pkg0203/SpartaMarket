# Generated by Django 4.2 on 2024-04-16 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', '남성'), ('F', '여성')], max_length=1),
        ),
    ]