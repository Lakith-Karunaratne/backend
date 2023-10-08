# Use an official Python runtime as a parent image
FROM python:3.11.5-slim

# Set environment variables for Python to run in unbuffered mode and disable pycache
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN poetry export --without-hashes --format=requirements.txt > requirements.txt

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . /app/

# Expose port 8000 to the outside world
EXPOSE 8000

# Define the command to run your FastAPI application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
