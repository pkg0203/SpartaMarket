from django import forms
from .models import Products,Comments

class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields =[
            "title",
            "content",
            "price",
            "image"
        ]

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = [
            'content',
        ]