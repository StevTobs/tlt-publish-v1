FROM python:3.8-slim-buster

# Install required packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    postgresql-client \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Copy the application code
COPY . .

# Set environment variables
ENV DJANGO_SETTINGS_MODULE=myprojecttlt.settings
ENV PYTHONUNBUFFERED=1

# Expose the port
EXPOSE 8000

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]