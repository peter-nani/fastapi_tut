# fastapi_tut

Teaching FastAPI

## Core & Data Handling
- **Pydantic (v2)**: Data validation library ensuring API data matches requirements
- **Starlette**: Lightweight ASGI framework providing routing, sessions, and sockets
- **AnyIO**: Asynchronous networking library for handling concurrent connections

## Database & Storage
- **SQLModel**: Merges Pydantic and SQLAlchemy for unified API and database classes
- **SQLAlchemy**: Python SQL toolkit for PostgreSQL, MySQL, and SQLite
- **Alembic**: Database migration tool for schema changes
- **Motor**: Asynchronous MongoDB driver
- **Beanie**: Async ODM for MongoDB with Pydantic support

## Servers & Performance
- **Uvicorn**: ASGI server for running FastAPI
- **Gunicorn**: Process manager for multiple Uvicorn instances
- **Redis**: In-memory data store for caching and sessions

## Testing & Utilities
- **Pytest**: Python testing framework
- **HTTPX**: Async-capable HTTP client
- **Python-Multipart**: File upload and form-data support
- **Loguru**: Modern logging library

## Security & Authentication
- **PyJWT**: JSON Web Token generation and verification
- **Passlib (with Bcrypt)**: Password hashing
- **Python-Jose**: Cryptographic tools for authentication

## Task Management & Communication
- **Celery**: Distributed task queue for background jobs
- **Flower**: Real-time monitoring dashboard for Celery

## Containerization & Orchestration
- **Docker**: Container packaging
- **Docker Compose**: Multi-container orchestration
- **Kubernetes (K8s)**: Container management at scale

## CI/CD
- **GitHub Actions**: Automated testing and deployment
- **SonarQube / Snyk**: Security vulnerability scanning

## Web Server & Networking
- **Nginx / Traefik**: Reverse proxy for SSL and load balancing
- **Certbot (Let's Encrypt)**: Free SSL certificate management

## Observability & Monitoring
- **Prometheus**: Real-time metrics collection
- **Grafana**: Performance dashboard
- **Sentry**: Error tracking
- **Loki / ELK Stack**: Centralized logging

## Infrastructure & Secrets
- **Terraform**: Infrastructure as Code
- **Pydantic Settings**: Environment variable management
- **AWS Secrets Manager / Vault**: Secrets storage

---

## Quick start

1. Create virtual env and install deps:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Run the app (dev):

```bash
export DATABASE_URL="sqlite:///./dev.db"
uvicorn app.main:app --reload
```

### Docs

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc
- OpenAPI spec: http://localhost:8000/openapi.json

### Alembic

- Set env var: `export DATABASE_URL=sqlite:///./dev.db`
- Generate migration: `alembic revision --autogenerate -m "create users"`
- Apply: `alembic upgrade head`

### Testing

```bash
pytest
```
