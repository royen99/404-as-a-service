# Quick Start Guide

## Get Up and Running in 30 Seconds ⚡

```bash
# 1. Setup environment
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env

# 2. Start the server
uvicorn app.main:app --reload

# 3. Test it out
curl http://localhost:8000/api/v1/404
```

## Live Example Requests

```bash
# Get a random 404 message
curl http://localhost:8000/api/v1/404

# List all available reasons
curl http://localhost:8000/api/v1/reasons

# Trigger catch-all 404 (any undefined path)
curl http://localhost:8000/oops/wrong/url
```

## What You Get

```json
{
  "status_code": 404,
  "error": "Not Found",
  "message": "This page is playing hide and seek",
  "reason": "Spoiler alert: it's really good at hiding",
  "category": "playful"
}
```

## Next Steps

- 📖 Read the full [README.md](README.md)
- 🧪 Run tests: `pytest -v --cov=app`
- 🐳 Try Docker: `cp docker-compose.yml.example docker-compose.yml && docker-compose up`
- 🎨 Add your own 404 messages in [data/reasons.json](data/reasons.json)
- 📚 Check API docs: http://localhost:8000/docs

## Useful Commands

```bash
# Development
uvicorn app.main:app --reload          # Start with hot reload
pytest -v --cov=app                    # Run tests with coverage
ruff check . && ruff format .          # Lint and format code

# Docker
docker-compose up --build              # Build and run in containers
docker-compose down -v                 # Stop and clean up

# Production
uvicorn app.main:app --host 0.0.0.0 --port 8000  # Production server
```

## Troubleshooting

**Port already in use?**
```bash
# macOS/Linux
lsof -ti:8000 | xargs kill -9

# Or change port
uvicorn app.main:app --port 8080
```

**Dependencies not installing?**
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

**Tests failing?**
```bash
# Make sure you're in the venv
source .venv/bin/activate
pytest -v
```

Need help? Check the [README.md](README.md) for more details! 🚀
