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
    content = forms.CharField(
        widget=forms.TextInput(attrs={
            'class':'form-control',
            }))
    class Meta:
        model = Comments
        fields = [
            'content',
        ]