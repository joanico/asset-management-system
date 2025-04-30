# Docker Setup for Django Mini-Project

This document provides instructions for setting up and running the Django asset management application using Docker in both development and production environments.

## Prerequisites

- Docker (>= 20.10.0)
- Docker Compose (>= 2.0.0)
- Git

## Project Structure

The Docker setup consists of:

- Development environment:
  - Django application with live code reloading
  - SQLite database with persistent volume
  - Redis for caching

- Production environment:
  - Django application served with Gunicorn
  - PostgreSQL database
  - Redis for caching
  - Nginx for serving static files and reverse proxy

## Development Setup

1. Clone the repository:
   ```
   git clone <repository-url>
   cd mini_project
   ```

2. Start the development environment:
   ```
   chmod +x dev.sh
   ./dev.sh
   ```

3. Access the application:
   - Django Admin: http://localhost:8000/admin/
   - Application: http://localhost:8000/

4. Development features:
   - Code changes are instantly reflected
   - Django debug toolbar is enabled
   - SQLite database is used for simplicity

## Production Setup

1. Create a `.env` file:
   ```
   cp .env.sample .env
   ```

2. Edit the `.env` file and update the values:
   - Set a strong SECRET_KEY
   - Update DATABASE_USER and DATABASE_PASSWORD
   - Add your domain to ALLOWED_HOSTS
   - Configure email settings

3. Deploy the application:
   ```
   chmod +x deploy.sh
   ./deploy.sh
   ```

4. Access the application:
   - Application: http://your-domain.com/
   - Admin: http://your-domain.com/admin/

## Database Backup

To backup the database and media files:

```
chmod +x backup.sh
./backup.sh
```

Backups are stored in the `backups` directory.

## Common Tasks

### Create a Django superuser

```
# For development
docker-compose exec web python manage.py createsuperuser

# For production
docker-compose -f docker-compose.prod.yml exec web python manage.py createsuperuser
```

### Check logs

```
# For development
docker-compose logs -f

# For production
docker-compose -f docker-compose.prod.yml logs -f
```

### Run Django management commands

```
# For development
docker-compose exec web python manage.py <command>

# For production
docker-compose -f docker-compose.prod.yml exec web python manage.py <command>
```

### Restart services

```
# For development
docker-compose restart

# For production
docker-compose -f docker-compose.prod.yml restart
```

## Security Considerations

For production deployments:

1. Always use strong, unique passwords for database and admin users
2. Keep the `.env` file secure and never commit it to version control
3. Regularly update Docker images and packages
4. Set up regular database backups
5. Consider implementing HTTPS with Let's Encrypt

## Troubleshooting

### Common issues:

1. Port conflicts: Make sure ports 8000 (dev) and 80 (prod) are available
2. Permission issues: Make sure scripts are executable with `chmod +x *.sh`
3. Database connection errors: Check the connection parameters in `.env`

For more help, check the container logs:
```
docker-compose -f docker-compose.prod.yml logs -f
```

## Additional Resources

- [Docker Documentation](https://docs.docker.com/)
- [Django Documentation](https://docs.djangoproject.com/)
- [Nginx Documentation](https://nginx.org/en/docs/) 