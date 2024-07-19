from django.urls import path
from .views import SliderViews

urlpatterns = [
    path('slider/', SliderViews.as_view(), name='slider')
]
