from rest_framework import serializers
from .models import Product, ProductImages


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImages
        fields = ('id', 'image')


class ProductSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True, source="images_set")

    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'body',
                  'pic', 'images', 'created_at')
