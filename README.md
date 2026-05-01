# SkyCast - Weather Intelligence Dashboard 🌦️

A professional, high-performance weather intelligence platform built with **Django**, **Redis**, and **Docker**. It features a premium Glassmorphism UI, live precipitation radar, and an interactive 15-day forecast.

---

## 🚀 Features
- **Live Radar**: Real-time precipitation map with animation controls (via RainViewer & Leaflet.js).
- **Interactive Analytics**: 7-day temperature and rain probability trends using Chart.js.
- **15-Day Forecast**: Comprehensive extended forecast with dynamic weather icons.
- **Astronomy Panel**: Tracking sunrise, sunset, and current moon phases.
- **PWA Ready**: Can be installed as a standalone app on Android and iOS.
- **Self-Documenting API**: Integrated Swagger and Redoc for external developers.
- **Smart Caching**: Redis (Upstash) integration to reduce API costs and improve speed.

---

## 🛠️ Tech Stack
- **Backend**: Python / Django / Django REST Framework
- **Caching**: Redis (Upstash for production)
- **Frontend**: Javascript (Vanilla), Tailwind CSS, Leaflet.js, Chart.js
- **DevOps**: Docker, Gunicorn, WhiteNoise

---

## 💻 Local Setup

### 1. Prerequisites
- Docker & Docker Desktop installed.
- A [Visual Crossing Weather API Key](https://www.visualcrossing.com/weather-api).

### 2. Configuration
Create a `.env` file in the root directory:
```bash
DJANGO_SECRET_KEY=your_random_secret_key
DEBUG=True
VISUAL_CROSSING_API_KEY=your_api_key_here
REDIS_URL=redis://redis:6379/0
WEATHER_CACHE_TTL=43200
ALLOWED_HOSTS=localhost,127.0.0.1
```

### 3. Run with Docker
```bash
docker-compose up --build
```
Access the app at: `http://localhost:8000`

---

## 🌐 Production Deployment (Koyeb / Render)

### 1. Environment Variables
When deploying, set the following in your host's dashboard:
- `DEBUG`: `False`
- `REDIS_URL`: Your **Upstash** `rediss://` connection string.
- `ALLOWED_HOSTS`: Your live domain (e.g., `skycast.onrender.com`).

### 2. Database
The project uses SQLite stored in the `database/` folder. This folder is ignored by Git. For production, the database is ephemeral (resets on restart). If you need persistent users, consider connecting a managed PostgreSQL database.

---

## 📚 API Documentation
Once the app is running, access the documentation at:
- **Swagger UI**: `/api/docs/`
- **Redoc**: `/api/redoc/`

---

## 📱 Mobile Installation (PWA)
1. Open the website on your phone.
2. Select **"Add to Home Screen"** from your browser menu.
3. The app will now appear on your home screen with the SkyCast icon!

---

## 🧹 Maintenance
- **Clear Cache**: `docker-compose exec redis redis-cli flushall`
- **Update Dependencies**: Update `requirements.txt` and run `docker-compose build --no-cache`.

---

**Developed with ❤️ by Antigravity**
