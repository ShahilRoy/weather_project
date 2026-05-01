# Use official Python runtime
FROM python:3.13-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=weather_project.settings

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir --root-user-action=ignore -r requirements.txt

# Copy project
COPY . /app/

# Create a non-root user for security
RUN useradd -m myuser && chown -R myuser:myuser /app
USER myuser

# Prepare static files for production
RUN python manage.py collectstatic --noinput

# Run the application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "weather_project.wsgi:application"]
