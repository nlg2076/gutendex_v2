# Use Python 3.9 base image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE gutendex.settings

# Install dependencies
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app

# Update pip
RUN python -m pip install --upgrade pip
RUN apt-get update && apt-get install -y netcat-openbsd

# Install requirements
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files
COPY . /app

# Expose the port
EXPOSE 8000

# Entry point
ENTRYPOINT ["/app/entrypoint.sh"]
