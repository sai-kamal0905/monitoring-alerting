# web/Dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install flask prometheus_client
CMD ["python", "app.py"]
