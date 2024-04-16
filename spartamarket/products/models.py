from django.db import models
from django.conf import settings

# Create your models here.
class Products(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="authors"
    )
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    is_selled = models.BooleanField(default=False)
    image = models.ImageField(
        upload_to="images/",
        #Null= True 와는 다름
        blank=True
    )