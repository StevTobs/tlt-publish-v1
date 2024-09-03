# Use the official Python 3.11 slim image (recommended for smaller image size)
FROM python:3.11-slim

# Set the working directory within the container to /app
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Copy your project code
COPY . .  
# Ensures project files are copied to the working directory

# Set the correct Django settings module environment variable
ENV DJANGO_SETTINGS_MODULE=myprojecttlt.settings  
# Replace 'myproject' with your actual project name

# Expose the Django development server port (optional, but recommended for accessibility)
EXPOSE 8000  
# Exposes port 8000 for server access

# Run the Django development server (use `gunicorn` for production)
CMD ["python", "manage.py", "runserver"]