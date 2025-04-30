#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Function to display messages
log() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1"
}

# Check if .env file exists
if [ ! -f .env ]; then
    log "Error: .env file not found. Please create one based on .env.sample"
    exit 1
fi

# Load environment variables
source .env

# Build and start production containers
log "Building production containers..."
docker-compose -f docker-compose.prod.yml build

log "Starting production services..."
docker-compose -f docker-compose.prod.yml up -d

log "Creating logs directory if it doesn't exist..."
mkdir -p logs

# Wait for the database to be ready
log "Waiting for database to be ready..."
sleep 10

# Run migrations
log "Running database migrations..."
docker-compose -f docker-compose.prod.yml exec web python manage.py migrate

# Collect static files
log "Collecting static files..."
docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input

log "Deployment completed successfully!"
log "Your application should be available at: http://localhost"
log "To view logs: docker-compose -f docker-compose.prod.yml logs -f" 