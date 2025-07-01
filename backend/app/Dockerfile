FROM python:3.9-slim

# Install curl
RUN apt-get update && apt-get install -y curl && apt-get clean
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Copy and make wait script executable
COPY wait-for-elasticsearch.sh /wait-for-elasticsearch.sh
RUN chmod +x /wait-for-elasticsearch.sh

EXPOSE 9567

# Use wait-for-elasticsearch before running uvicorn
CMD ["/wait-for-elasticsearch.sh", "http://elasticsearch:9200", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "9567"]
