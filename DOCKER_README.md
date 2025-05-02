# Docker Design & Usage Guide

## 1. Goals
- Provide a reproducible, isolated environment for development and production.
- Simplify local development with hot-reloading and easy dependency management.
- Enable robust, scalable deployment with Docker Compose.

## 2. Technical Specifications

### Local Development
- Uses Docker Compose to run Django, Redis, and SQLite.
- Code changes are reflected instantly (volume mounting).
- Debug mode enabled.

### Production
- Uses Docker Compose to run Django (with Gunicorn), PostgreSQL, Redis, and Nginx.
- Static/media files served by Nginx.
- Environment variables for secrets and configuration.
- Debug mode disabled.

## 3. Project Structure
```
mini_project/
│
├── Dockerfile
├── docker-compose.yml
├── docker-compose.prod.yml
├── .env.sample
├── .dockerignore
├── nginx/
│   └── conf.d/
│       └── default.conf
├── mini_project/
│   └── settings/
│       ├── base.py
│       ├── development.py
│       └── production.py
├── asset_app/
├── manage.py
├── requirements.txt
└── ... (other Django files)
```

## 4. Dockerfile
- Based on `python:3.11-slim`.
- Installs system dependencies, Python requirements, and copies project files.
- Entrypoint script handles migrations, static collection, and server start.

## 5. Docker Compose Files

### docker-compose.yml (Development)
- Services: `web` (Django), `redis`
- Uses SQLite for simplicity.
- Mounts code for live reload.
- Exposes port 8000.

### docker-compose.prod.yml (Production)
- Services: `web` (Django/Gunicorn), `db` (PostgreSQL), `redis`, `nginx`
- Uses PostgreSQL for data.
- Nginx serves static/media and proxies to Django.
- Exposes port 80.

## 6. Environment Variables
- Managed via `.env` file (copy from `.env.sample`).
- Includes `SECRET_KEY`, `ALLOWED_HOSTS`, database credentials, and security settings.

## 7. Django Settings
- `base.py`: Common settings.
- `development.py`: Debug, SQLite, local cache.
- `production.py`: Reads all sensitive/configurable values from environment variables, uses PostgreSQL, secure cookies, CSRF trusted origins, etc.

## 8. Nginx Configuration
- Proxies requests to Django.
- Serves static and media files.
- Handles error pages.

## 9. Scripts
- `dev.sh`: Builds and runs the development environment.
- `deploy.sh`: Builds and runs the production environment, runs migrations, collects static files.
- `backup.sh`: Backs up database and media files.

## 10. .dockerignore
- Excludes files/folders not needed in the Docker image (e.g., `.git`, `__pycache__`, local data, etc.).

---

# Running the Project Locally with Docker

1. **Copy and configure environment variables:**
   ```bash
   cp .env.sample .env
   # Edit .env as needed for local development
   ```

2. **Build and start the development environment:**
   ```bash
   chmod +x dev.sh
   ./dev.sh
   ```

3. **Access the app:**
   - Visit [http://localhost:8000/](http://localhost:8000/) in your browser.

4. **Common dev commands:**
   - View logs: `docker-compose logs -f`
   - Run management commands: `docker-compose exec web python manage.py <command>`

---

# Deploying to Production with Docker

1. **Provision a server (e.g., DigitalOcean, AWS) and install Docker & Docker Compose.**

2. **Copy your project to the server and set up the environment:**
   ```bash
   cp .env.sample .env
   # Edit .env with production values (strong SECRET_KEY, DB credentials, ALLOWED_HOSTS, etc.)
   ```

3. **Build and start the production environment:**
   ```bash
   chmod +x deploy.sh
   ./deploy.sh
   ```

4. **Access the app:**
   - Visit `http://your.server.ip/` or your domain in a browser.

5. **(Optional) Set up HTTPS:**
   - Use Let's Encrypt and update Nginx config for SSL.

6. **Monitor and maintain:**
   - View logs: `docker-compose -f docker-compose.prod.yml logs -f`
   - Backup: `./backup.sh`

---

# Summary Table

| Step                | Local Development           | Production Deployment         |
|---------------------|----------------------------|------------------------------|
| Compose file        | docker-compose.yml          | docker-compose.prod.yml       |
| DB                  | SQLite                     | PostgreSQL                   |
| Static/media        | Served by Django            | Served by Nginx              |
| Entrypoint          | dev.sh                     | deploy.sh                    |
| Access              | http://localhost:8000/     | http://your.server.ip/       |
| Env config          | .env                       | .env                         |

---

# Existing Docker Setup Instructions

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