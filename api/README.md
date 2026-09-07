# FastAPI API

Minimal and strict template for the inference API.

## Getting Started

```powershell
uv sync
uv run uvicorn api:app --app-dir src --reload
```

Then open <http://127.0.0.1:8000/docs>.

## Available Endpoint

```text
GET /health -> {"status":"ok"}
```

Pydantic schemas reject unknown fields and implicit type coercion.
