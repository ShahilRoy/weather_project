from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import get_weather_data
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'index.html'
from django.core.cache import cache
from django.conf import settings
from rest_framework.throttling import UserRateThrottle

class WeatherView(APIView):
    def get(self, request, city):
        """
        GET /api/weather/{city}/
        Fetches weather data for the specified city.
        """
        try:
            weather_data = get_weather_data(city)
            return Response(weather_data)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
