# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Install required packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    postgresql-client \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# (Optional) Set environment variables
# ENV DJANGO_SETTINGS_MODULE=myprojecttlt.settings
# ENV PYTHONUNBUFFERED=1

# Expose the port on which the Django app will run
EXPOSE 8001

# Run the Django development server on port 8001
CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]
