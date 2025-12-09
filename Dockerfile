# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements and install necessary libraries
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files
COPY . .

# Expose the port used by Flask
EXPOSE 5000

# Start the Flask application
# 0.0.0.0 allows access from outside the container
CMD ["sh", "-c", "python inserimento_ricette.py && python app.py"]


