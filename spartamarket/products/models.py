from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.


class HashTag(models.Model):
    title = models.CharField(max_length=50)


class Products(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="authors"
    )
    price = models.IntegerField(validators=[MinValueValidator(0)])
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    is_selled = models.BooleanField(default=False)
    image = models.ImageField(
        upload_to="images/",
        default='./images/default_image.PNG',
        # Null= True 와는 다름
        blank=True
    )
    is_viewed = models.IntegerField(default=0)
    hashtags = models.ManyToManyField(
        HashTag,
        blank=True,
        related_name="hashtags"
    )


class Comments(models.Model):
    products = models.ForeignKey(
        Products, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="c_authors"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
