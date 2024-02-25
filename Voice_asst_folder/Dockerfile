####################################################################

# Use the official Python 3.11 image
FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    portaudio19-dev \
    # Additional dependencies as needed
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

COPY . /app

# Copy the requirements file into the container at /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000
EXPOSE 5000

# Run the Python application
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]

