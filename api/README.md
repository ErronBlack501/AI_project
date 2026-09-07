# API FastAPI

Template minimal et strict pour l'API d'inference.

## Demarrage

```powershell
uv sync
uv run uvicorn api:app --app-dir src --reload
```

Puis ouvrir <http://127.0.0.1:8000/docs>.

## Endpoint disponible

```text
GET /health -> {"status":"ok"}
```

Les schemas Pydantic refusent les champs inconnus et la coercition implicite des types.
