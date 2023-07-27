# Use the official Python base image from Docker Hub
FROM python:3.11.4

# Set the working directory inside the container
WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "api/main.py"]
