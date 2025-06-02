# Well-Bot_v6

## File Directory Structure
```
WELL-BOT_V6/
├── .secrets/                # Stores secret tokens or API keys (e.g. Kaggle credentials)
├── app/                     # Main backend application logic
│   ├── api/                 # API route handlers (e.g. POST /speech)
│   ├── core/                # Configuration and database initialization
│   ├── crud/                # Business logic and DB interaction for speech data
│   ├── models/              # Pydantic data schemas for request/response validation
│   ├── services/            # Modular ML components: emotion, sentiment, transcription, generation
│
├── data/                    # Local data storage
│   └── audio_raw/           # Raw downloaded datasets for training/analysis
│       ├── crema/           # CREMA-D dataset
│       ├── ravdess/         # RAVDESS dataset
│       └── tess/            # TESS dataset
│
├── scripts/                 # Custom scripts (e.g., dataset downloaders, preprocessors)
├── test/                    # Unit and integration tests for speech APIs and services
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