# Use an official Python image
FROM python:3.11-slim
# Set working directory
WORKDIR /app
# Copy the current directory content into the container at /app
COPY . .
# Install the required libraries
RUN pip install -r requirements.txt
# Expose the port
EXPOSE 5000
# Run the Flask application
CMD ["python", "app.py"]
