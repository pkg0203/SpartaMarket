from django.db import models
from django.contrib.auth.models import AbstractUser
from products.models import Products


class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = 'M', '남성'
        FEMALE = 'F', '여성'
    age = models.IntegerField()
    gender = models.CharField(
        choices=GenderChoices.choices,
        max_length=1,
        blank=False
    )
    follow = models.ManyToManyField(
        'self',
        related_name='followers',
        symmetrical=False
    )
    jjim = models.ManyToManyField(
        Products,
        related_name='jjimed',
        symmetrical=False
    )
    created_at = models.DateTimeField(auto_now_add=True)
    profile_image = models.ImageField(
        default='./images/default_profile.png',
        upload_to='images/',
    )
