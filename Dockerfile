FROM python:3.8

# Install the required packages


# Copy the application code to the container
COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

# Expose the port for the service to run on
EXPOSE 8000


# Start the service
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
