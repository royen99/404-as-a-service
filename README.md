# 404-as-a-Service

[![CI Tests](https://github.com/royen99/404-as-a-service/actions/workflows/ci.yml/badge.svg)](https://github.com/royen99/404-as-a-service/actions/workflows/ci.yml)
[![codecov](https://codecov.io/github/royen99/404-as-a-service/graph/badge.svg?token=9MHZ3BQ025)](https://codecov.io/github/royen99/404-as-a-service)[![Python 3.14+](https://img.shields.io/badge/python-3.14+-blue.svg)](https://www.python.org/downloads/)
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> *Because even errors deserve personality*

A microservice that serves creative, witty 404 errors for any website. Why settle for boring "Not Found" messages when you can have fun with them?

## Features

- **Random creative 404 messages** - 20+ hand-crafted reasons spanning 12 categories
- **CSS powered HTML UI** - Tailwind CSS-powered pages with category-specific themes & animations
- **FastAPI-powered** - Async, fast, and production-ready
- **Containerized** - Docker support for easy deployment
- **Simple API** - Both JSON API and gorgeous HTML responses
- **Category Theming** - Each error category has unique colors, gradients, and animations
- **Fully tested** - Comprehensive test coverage

## Quick Start

### Local Development

```bash
# Setup
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env

# Run the server
uvicorn app.main:app --reload

# Visit http://localhost:8000/docs for interactive API docs
```

### Docker

```bash
# Copy example docker-compose
cp docker-compose.yml.example docker-compose.yml

# Build and run
docker-compose up --build

# Service available at http://localhost:8000
```

## API Usage

### Get a Random 404 (JSON)

```bash
curl http://localhost:8000/api/v1/404
```

**Response:**
```json
{
  "status_code": 404,
  "error": "Not Found",
  "message": "This page is playing hide and seek",
  "reason": "Spoiler alert: it's really good at hiding",
  "category": "playful"
}
```

### Get a Beautiful HTML 404

Simply visit any undefined route in your browser:
```
http://localhost:8000/some/random/path
```

Or use the dedicated 404 page:
```
http://localhost:8000/404
```

### Get Category-Specific 404s

Want a specific theme? Add a category parameter:
```
http://localhost:8000/404?category=gaming
http://localhost:8000/404?category=tech-humor
http://localhost:8000/404?category=philosophical
```

**Available categories:**
- `philosophical` - Deep, existential vibes 🧘
- `sassy` - Attitude with style 💅
- `playful` - Fun and lighthearted 🎮
- `absurd` - Wonderfully weird 🌀
- `tech-humor` - For the nerds 💻
- `sarcastic` - Delightfully snarky 😏
- `workplace` - Office life humor 💼
- `fantasy` - Magical and mystical 🐉
- `modern` - Internet culture 📱
- `gaming` - For gamers 🎯
- `science` - Quantum and nerdy ⚛️
- `dark-humor` - A bit edgy 💀

### List All Available Reasons

```bash
curl http://localhost:8000/api/v1/reasons
```

**Response:**
```json
{
  "total": 20,
  "reasons": [
    {
      "message": "The page wandered off to find itself",
      "reason": "Last seen at a digital ashram meditating on its purpose",
      "category": "philosophical"
    },
    ...
  ]
}
```

### Catch-All 404s

Any undefined route automatically returns a creative 404:

```bash
curl http://localhost:8000/any/random/path
```

## Integration Examples

### JavaScript Fetch

```javascript
async function get404Message() {
  const response = await fetch('http://your-domain.com/api/v1/404');
  const data = await response.json();
  return data;
}
```

### Python Requests

```python
import requests

response = requests.get('http://your-domain.com/api/v1/404')
error_data = response.json()
print(f"{error_data['message']}: {error_data['reason']}")
```

### HTML Integration

Embed in your error page:
```html
<iframe src="http://your-domain.com/404?category=tech-humor"
        style="width:100%; height:600px; border:none;">
</iframe>
```

Or redirect users:
```javascript
window.location.href = 'http://your-domain.com/404?category=gaming';
```

## Project Structure

```
404-as-a-service/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI app entry point
│   ├── core/
│   │   ├── config.py        # Settings & configuration
│   ├── routers/
│   │   ├── api.py           # JSON API endpoints
│   │   └── web.py           # HTML routes with templates
│   ├── services/
│   │   └── reason_service.py # Business logic
│   └── templates/
│       ├── base.html        # Base template with Tailwind
│       ├── home.html        # Landing page
│       └── 404.html         # Rendered 404 pages
├── data/
│   └── reasons.json         # 404 messages database
├── tests/
│   ├── test_api.py          # API endpoint tests
│   └── test_services.py     # Service layer tests
├── Dockerfile
├── docker-compose.yml.example
└── requirements.txt
```

## Development

### Running Tests

```bash
# Run all tests with coverage
pytest -v --cov=app

# Generate HTML coverage report
pytest --cov=app --cov-report=html
open htmlcov/index.html
```

### Code Quality

```bash
# Lint and format with Ruff
ruff check .
ruff format .
```

### Adding New 404 Reasons

Edit [data/reasons.json](data/reasons.json) and add your creative messages:

```json
{
  "message": "Your witty 404 message",
  "reason": "The humorous explanation",
  "category": "your-category"
}
```

Categories: `philosophical`, `sassy`, `playful`, `absurd`, `tech-humor`, `sarcastic`, `workplace`, `fantasy`, `modern`, `gaming`, `science`, `dark-humor`

## Configuration

Environment variables (see [.env.example](.env.example)):

| Variable | Default | Description |
|----------|---------|-------------|
| `APP_NAME` | 404-as-a-Service | Application name |
| `DEBUG` | false | Enable debug mode |
| `HOST` | 0.0.0.0 | Server host |
| `PORT` | 8000 | Server port |
| `REASONS_FILE` | data/reasons.json | Path to reasons file |


## Contributing

Found a great 404 message? Have an improvement? PRs welcome!

1. Fork the repo
2. Create a feature branch
3. Add your changes
4. Run tests: `pytest`
5. Submit a PR

## License

MIT - Because sharing is caring 💖

## Credits

Built with FastAPI, fueled by coffee ☕, and inspired by the internet's best 404 pages.

---

*"The best error messages are the ones that make you smile" - Ancient DevOps Proverb*
