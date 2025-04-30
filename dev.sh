#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Function to display messages
log() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1"
}

# Build and start development containers
log "Building development containers..."
docker-compose build

log "Starting development services..."
docker-compose up -d

# Create data directory if it doesn't exist
log "Creating data directory if it doesn't exist..."
mkdir -p data

# Run migrations
log "Running database migrations..."
docker-compose exec web python manage.py migrate

log "Development environment is ready!"
log "Your application should be available at: http://localhost:8000"
log "To view logs: docker-compose logs -f"
log "To stop the containers: docker-compose down" 