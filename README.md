# Well-Bot_v6

## File Directory Structure
```
wellbot_backend/
├── app/                     # Application logic
│   ├── api/                 # API endpoints (routes)
│   ├── core/                # Configuration, MongoDB connection
│   ├── crud/                # Business logic and DB access
│   ├── models/              # Pydantic models (schemas)
│   ├── services/            # Future plug-ins (e.g., RAG/Langroid)
│   └── main.py              # FastAPI app instance and startup
│
├── tests/                   # Unit and integration tests
│
├── .env                     # Environment variables (DB URI, secrets)
├── Dockerfile               # FastAPI Docker setup
├── docker-compose.yml       # Full stack (FastAPI + MongoDB)
├── requirements.txt         # Python dependencies
└── README.md                # Project intro and instructions
```

### Folder Purpose
| Folder/File          | Purpose                                                                |
| -------------------- | ---------------------------------------------------------------------- |
| `app/`               | Root of your actual backend logic.                                     |
| `app/api/`           | Your REST API route handlers (e.g., `@router.post("/emotions")`)       |
| `app/core/`          | Configuration (e.g., `.env` loader), MongoDB client init               |
| `app/crud/`          | Database interaction logic (e.g., create, get, update emotion records) |
| `app/models/`        | Pydantic models for request/response validation                        |
| `app/services/`      | Future subsystems (Langroid, ML models, etc.)                          |
| `app/main.py`        | Main entry point — creates FastAPI app, includes routes                |
| `tests/`             | Write unit tests for endpoints, DB logic, RAG plugins                  |
| `.env`               | Holds DB URIs, secret keys, etc. — loaded via `pydantic.BaseSettings`  |
| `Dockerfile`         | Builds your FastAPI app container                                      |
| `docker-compose.yml` | Orchestrates FastAPI + MongoDB together                                |
| `requirements.txt`   | Specifies Python dependencies                                          |
| `README.md`          | Developer guide and usage notes                                        |

