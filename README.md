# Well-Bot_v6

## File Directory Structure
```
WELL-BOT_V6/
├── app/
│   ├── api/             # API endpoints (routes)
│   ├── core/            # Config and MongoDB connection
│   ├── crud/            # CRUD logic for DB operations
│   ├── models/          # Pydantic request/response schemas
│   ├── services/        # Future subsystems (Langroid, ML, etc.)
│   └── main.py          # FastAPI app entry point
│
├── test/                # Unit tests
├── .env                 # Environment variables
├── Dockerfile           # Docker image definition
├── docker-compose.yml   # Orchestrates API + MongoDB
├── requirements.txt     # Python dependencies
└── README.md            # You're here

```

### Folder Purpose
| Path                 | Purpose                                                        |
| -------------------- | -------------------------------------------------------------- |
| `app/`               | Main backend codebase                                          |
| `app/api/`           | API route handlers (e.g., `POST /emotions`)                    |
| `app/core/`          | Loads `.env` configs & MongoDB setup                           |
| `app/crud/`          | Business logic and DB interactions (e.g., `insert_emotion`)    |
| `app/models/`        | Defines data schemas using Pydantic (e.g., `EmotionCreate`)    |
| `app/services/`      | Reserved for plugins: Langroid, ML inference, etc.             |
| `app/main.py`        | Creates FastAPI app and binds routers                          |
| `test/`              | Test suite for API & logic using `pytest`                      |
| `.env`               | Holds config (like MongoDB URI) — never commit secrets to Git! |
| `Dockerfile`         | Builds the FastAPI container                                   |
| `docker-compose.yml` | Brings up FastAPI and MongoDB services together                |
| `requirements.txt`   | All Python package dependencies                                |


## Getting Started
### 1. Clone and setup
```bash
git clone <your-repo-url>
cd WELL-BOT_V6
```

### 2. Define environment variables
Update the `.env` file, e.g.
```bash
env
MONGODB_URL=mongodb://mongodb:27017
```

### 3. Run the backend and database
```bash
docker-compose up --build
```
* Backend will be live at: `http://localhost:8000`
* Docs auto-generated at: `http://localhost:8000/docs`

## Running Tests
```bash
pytest
```
* Sample test lives in test/test_emotion.py. Add more as features grow.