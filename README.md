# Well-Bot_v6
* FastAPI Template: [https://fastapi.tiangolo.com/project-generation/]([url](https://fastapi.tiangolo.com/project-generation/))
## File Directory Structure
```
WELL-BOT_V6/
├── app/
│   ├── api/                 # API endpoints (routes)
│   ├── core/                # Config and MongoDB connection
│   ├── crud/                # CRUD logic for DB operations
│   ├── models/              # Pydantic request/response schemas
│   ├── services/            # Machine Learning Models and Subsystems (Langroid, ML, etc.)
│   └── main.py              # FastAPI app entry point
│
├── data/
│   ├── audio_raw/
│
├── scripts/                 # Custom training + preprocessing scripts
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
git clone https://github.com/eefei22/well-bot_v6.git
cd WELL-BOT_V6
```

### 2. Check out  `requirements.txt`
* Make changes to include dependecies necessary for your own environment
* Then `pip install -r requirements.txt`

# NOTE:
* venv files, raw data files, large pre-trained models etc. should not be pushed into github
* Check `.gitignore` and modify accordingly before any commits.
