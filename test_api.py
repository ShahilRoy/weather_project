import os
import django
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'weather_project.settings')
django.setup()

from weather_api.utils import get_weather_data

try:
    print("Fetching weather for Kolkata...")
    data = get_weather_data('Kolkata')
    print("SUCCESS!")
    print(f"Address: {data.get('resolvedAddress')}")
    print(f"Current Temp: {data.get('currentConditions', {}).get('temp')}°C")
except Exception as e:
    print(f"FAILED: {e}")
