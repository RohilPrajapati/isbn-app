FROM python:3.11-slim

# Set workdir
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY . .

# migrate db
RUN python manage.py migrate --noinput

# Collect static files (optional if you use Django static serving)
# RUN python manage.py collectstatic --noinput

# Gunicorn as the WSGI server
CMD ["gunicorn", "bookmandala_proj.wsgi:application", "--bind", "0.0.0.0:8000"]
