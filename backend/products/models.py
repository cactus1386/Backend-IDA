from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(default='')
    body = RichTextField(default='')
    pic = models.ImageField(upload_to='uploads/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ProductImages(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='images_set')
    image = models.ImageField(upload_to='uploads/')
