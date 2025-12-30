# API Usage

## Quick examples

Get list of users:

```bash
curl http://localhost:8000/api/v1/users/
```

Create a user:

```bash
curl -X POST "http://localhost:8000/api/v1/users/" -H "Content-Type: application/json" -d '{"name":"Alice","email":"alice@example.com","password":"secret"}'
```

Interactive docs:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

You can download the OpenAPI spec at `http://localhost:8000/openapi.json`.
