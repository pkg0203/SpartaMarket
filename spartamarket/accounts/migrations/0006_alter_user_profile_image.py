# Generated by Django 4.2 on 2024-04-18 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_user_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(default='./images/default_profile.png', upload_to='images/'),
        ),
    ]
