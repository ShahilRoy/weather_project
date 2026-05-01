from django.urls import path
from .views import WeatherView, HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('weather/<str:city>/', WeatherView.as_view(), name='weather-detail'),
]
