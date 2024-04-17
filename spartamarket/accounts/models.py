from django.db import models
from django.contrib.auth.models import AbstractUser


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