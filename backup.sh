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

# Create backups directory if it doesn't exist
BACKUP_DIR="backups"
mkdir -p $BACKUP_DIR

# Generate filename with timestamp
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
BACKUP_FILENAME="${BACKUP_DIR}/backup_${TIMESTAMP}.sql"

log "Creating database backup..."

# For PostgreSQL in production
if [[ "$DJANGO_SETTINGS_MODULE" == *"production"* ]]; then
    # Create PostgreSQL backup
    docker-compose -f docker-compose.prod.yml exec db pg_dump \
        -U $DB_USER \
        -d $DB_NAME \
        -f /tmp/backup.sql
    
    # Copy backup from container to host
    docker-compose -f docker-compose.prod.yml cp db:/tmp/backup.sql $BACKUP_FILENAME
    
    # Create media files backup
    log "Creating media files backup..."
    MEDIA_BACKUP="${BACKUP_DIR}/media_${TIMESTAMP}.tar.gz"
    docker-compose -f docker-compose.prod.yml exec web tar -zcf /tmp/media_backup.tar.gz -C /app mediafiles
    docker-compose -f docker-compose.prod.yml cp web:/tmp/media_backup.tar.gz $MEDIA_BACKUP
else
    # For SQLite in development
    log "Creating SQLite backup..."
    cp db.sqlite3 "${BACKUP_FILENAME}.sqlite3"
    
    # Create media files backup if they exist
    if [ -d "mediafiles" ]; then
        log "Creating media files backup..."
        MEDIA_BACKUP="${BACKUP_DIR}/media_${TIMESTAMP}.tar.gz"
        tar -zcf $MEDIA_BACKUP mediafiles
    fi
fi

log "Backup completed: $BACKUP_FILENAME"
log "Don't forget to periodically transfer these backups off-site!" 