from django.test import TestCase, Client
from django.urls import reverse
from unittest.mock import patch

class WeatherViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('weather-detail', args=['mumbai'])

    @patch('weather_api.utils.get_weather_data')
    def test_weather_success(self, mock_get_weather_data):
        """Test successful weather fetch."""
        mock_data = {
            'resolvedAddress': 'Mumbai, India',
            'currentConditions': {'temp': 28, 'conditions': 'Sunny', 'humidity': 70},
            'days': [
                {'datetime': '2023-10-27', 'tempmax': 30, 'tempmin': 25},
                {'datetime': '2023-10-28', 'tempmax': 29, 'tempmin': 24},
            ]
        }
        mock_get_weather_data.return_value = mock_data

        response = self.client.get(self.url)
        
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, mock_data)
        mock_get_weather_data.assert_called_once_with('mumbai')

    @patch('weather_api.utils.get_weather_data')
    def test_weather_city_not_found(self, mock_get_weather_data):
        """Test city not found error."""
        mock_get_weather_data.side_effect = ValueError("City not found")

        response = self.client.get(self.url)
        
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json())

    @patch('weather_api.utils.get_weather_data')
    def test_weather_api_error(self, mock_get_weather_data):
        """Test API failure."""
        mock_get_weather_data.side_effect = Exception("API Error")

        response = self.client.get(self.url)
        
        self.assertEqual(response.status_code, 500)
        self.assertIn('error', response.json())


class HomeViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('weather_api:home')

    def test_home_view(self):
        """Test home page renders successfully."""
        response = self.client.get(self.url)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
