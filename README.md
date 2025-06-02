# Well-Bot_v6

## File Directory Structure
```
WELL-BOT_V6/
├── app/
│   ├── api/                 # API endpoints (routes)
│   ├── core/                # Config and MongoDB connection
│   ├── crud/                # CRUD logic for DB operations
│   ├── models/              # Pydantic request/response schemas
│   ├── services/            # Future subsystems (Langroid, ML, etc.)
│   └── main.py              # FastAPI app entry point
│
├── data/
│   ├── audio_raw/
│
├── scripts/
│
├── test/                    # Unit tests
├── .env                     # Environment variables
├── Dockerfile               # Docker image definition
├── docker-compose.yml       # Orchestrates API + MongoDB
├── requirements.txt         # Python dependencies
└── README.md                # You're here


```

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
