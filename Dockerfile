# Use an official lightweight Python image
FROM python:3.12-slim

# Set work directory inside the container
WORKDIR /app

# Copy requirements first (for better caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Expose port (Flask default)
EXPOSE 5000

# Command to run the app
CMD ["python", "app.py"]
