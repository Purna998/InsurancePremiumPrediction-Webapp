FROM python:3.11-slim-buster

# Prevent Python from writing .pyc files and buffering stdout
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose port (Render sets $PORT at runtime)
EXPOSE 8000

# Start using gunicorn, bind to 0.0.0.0:$PORT
CMD gunicorn insurance.wsgi:application --bind 0.0.0.0:$PORT --workers 4 --threads 2 --timeout 120
