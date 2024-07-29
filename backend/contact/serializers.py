from rest_framework import serializers
from .models import Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['name', 'company', 'email', 'phone',
                  'message', 'attachment', 'created_at']

    def validate(self, data):
        if not data.get('name'):
            raise serializers.ValidationError("Name is required")
        if not data.get('phone'):
            raise serializers.ValidationError("Phone number is required")
        if not data.get('message'):
            raise serializers.ValidationError("Message is required")
        return data
