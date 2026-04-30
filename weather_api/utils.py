import requests
from django.core.cache import cache
from django.conf import settings

def get_weather_data(city):
    """
    Fetch weather data for a given city.
    Checks Redis cache first. If it's a miss, calls the Visual Crossing API.
    """
    # 1. Generate a unique cache key for the city
    cache_key = f"weather_{city.lower().replace(' ', '_')}"
    
    # 2. Check Redis cache
    cached_data = cache.get(cache_key)
    if cached_data:
        return cached_data

    # 3. Cache miss - Call Visual Crossing API
    api_key = settings.VISUAL_CROSSING_API_KEY
    if not api_key:
        raise ValueError("Visual Crossing API key is not configured in settings.")

    base_url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}"
    params = {
        'key': api_key,
        'unitGroup': 'metric',
        'include': 'current',
        'contentType': 'json'
    }

    try:
        response = requests.get(base_url, params=params, timeout=10)
        response.raise_for_status()
        weather_data = response.json()
        
        # 4. Store in Redis cache
        # Use the configured TTL from settings
        cache.set(cache_key, weather_data, timeout=settings.WEATHER_CACHE_TTL)
        
        return weather_data

    except requests.exceptions.RequestException as e:
        # Log the error or raise a custom exception
        raise Exception(f"Failed to fetch weather data for {city}: {str(e)}")
