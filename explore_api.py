import os
import django
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'weather_project.settings')
django.setup()

from weather_api.utils import get_weather_data

print("Fetching full API response for Kolkata...\n")
data = get_weather_data('Kolkata')

# ── Top-level fields ──────────────────────────────────────
print("=" * 60)
print("TOP-LEVEL FIELDS:")
print("=" * 60)
for key, val in data.items():
    if key not in ('days', 'currentConditions', 'alerts', 'stations'):
        print(f"  {key}: {val}")

# ── Current Conditions ────────────────────────────────────
print("\n" + "=" * 60)
print("CURRENT CONDITIONS FIELDS:")
print("=" * 60)
for key, val in data.get('currentConditions', {}).items():
    print(f"  {key}: {val}")

# ── Day[0] fields (today) ─────────────────────────────────
print("\n" + "=" * 60)
print("DAY OBJECT FIELDS (today):")
print("=" * 60)
day0 = data['days'][0]
for key, val in day0.items():
    if key != 'hours':
        print(f"  {key}: {val}")

# ── Hour[0] fields (first hour) ───────────────────────────
print("\n" + "=" * 60)
print("HOUR OBJECT FIELDS (hour 0 of today):")
print("=" * 60)
if day0.get('hours'):
    for key, val in day0['hours'][0].items():
        print(f"  {key}: {val}")
else:
    print("  No hourly data found!")

# ── Alerts ────────────────────────────────────────────────
print("\n" + "=" * 60)
print("ALERTS:")
print("=" * 60)
alerts = data.get('alerts', [])
if alerts:
    for a in alerts:
        print(f"  {a}")
else:
    print("  No active alerts.")

# ── Stations ──────────────────────────────────────────────
print("\n" + "=" * 60)
print(f"WEATHER STATIONS ({len(data.get('stations', {}))} available):")
print("=" * 60)
for sid, sdata in list(data.get('stations', {}).items())[:3]:
    print(f"  {sid}: {sdata}")

print(f"\nTotal days in response: {len(data['days'])}")
print(f"Total hours in day[0]: {len(day0.get('hours', []))}")
