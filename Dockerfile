FROM python:3.13-slim

WORKDIR /app

# Install system dependencies if needed
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy and install python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend and static directories
COPY backend/ ./backend/
COPY static/ ./static/

# Cloud Run binds to $PORT environment variable, defaulting to 8080
ENV PORT=8080
EXPOSE 8080

# Run FastAPI app dynamically binding to $PORT
CMD ["sh", "-c", "python -m uvicorn backend.main:app --host 0.0.0.0 --port ${PORT}"]
