from rest_framework import status
from .serializers import ContactSerializer
from rest_framework.generics import ListCreateAPIView
from .models import Contact


class ContactViews(ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
