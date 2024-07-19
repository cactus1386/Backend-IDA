from django.shortcuts import render
from .serializers import SliderSerializer
from .models import Slider
from rest_framework.generics import ListCreateAPIView

# Create your views here.


class SliderViews(ListCreateAPIView):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer
