# TODO App

Simple TODO list API built with FastAPI. Demo project for CI/CD lecture (Software Design, ITMO).

## Endpoints

| Method   | Path             | Description       |
|----------|------------------|-------------------|
| `GET`    | `/`              | Web UI            |
| `GET`    | `/health`        | Health check      |
| `GET`    | `/tasks`         | List all tasks    |
| `POST`   | `/tasks`         | Create a task     |
| `DELETE` | `/tasks/{id}`    | Delete a task     |

## Run locally

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

## Run tests

```bash
pytest --cov=main --cov-report=term-missing
```

## CI/CD

- **CI** (`.github/workflows/ci.yaml`) — lint (flake8) + tests (pytest) on push/PR to `main`
- **CD** (`.github/workflows/cd.yaml`) — deploy to VPS after successful CI or manual trigger
