# Use the official Python 3.11 image
FROM python:3.11-slim

# Set the workdir to /app
WORKDIR /tltapp

# Copy requirements.txt and install
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Copy the project code
COPY . ./

# Set the environment variable
ENV DJANGO_SETTINGS_MODULE=myproject.settings

# Run the Django development server
CMD ["python", "manage.py", "runserver"]