# Well-Bot_v6

## System Overview

Well-Bot_v6 is a modular FastAPI-based backend designed to process spoken input, analyze emotional state and sentiment, generate empathetic responses using an LLM, and synthesize those responses into speech. It supports multilingual interactions (including Malay, English, and Indonesian), and is built to integrate into a Raspberry Pi-based wellness droid. The system uses HuggingFace Transformers, DeepSeek API, and Google TTS for core functionality.

## File Directory Structure
```
WELL-BOT_V6/
├── .secrets/                # Stores secret tokens or API keys (e.g. Kaggle credentials)
├── app/                     # Main backend application logic
│   ├── api/                 # API route handlers (e.g. POST /analyze-speech)
│   ├── core/                # Configuration and database initialization
│   ├── crud/                # Business logic and DB interaction for speech data
│   ├── models/              # Pydantic data schemas for request/response validation
│   ├── services/            # Modular ML components: emotion, sentiment, transcription, generation, TTS
│
├── data/                    # Local data storage
│   ├── audio_raw/           # Raw downloaded datasets for training/analysis
│   │   ├── crema/           # CREMA-D dataset
│   │   ├── ravdess/         # RAVDESS dataset
│   │   └── tess/            # TESS dataset
│   └── tts_output/          # Synthesized speech audio outputs (MP3)
│
├── scripts/                 # Custom scripts (e.g., dataset downloaders, preprocessors)
├── test/                    # Unit and integration tests for speech APIs and services
├── .env                     # Environment variables
├── Dockerfile               # Docker image definition
├── docker-compose.yml       # Orchestrates API + MongoDB
├── requirements.txt         # Python dependencies
└── README.md                # This File
```

## Core `.py` Files and Responsibilities

### `app/api`

| `.py` File | Main Functionality | Key Drivers (How functionality is achieved) |
| ----- | ----- | ----- |
| **`speech.py`** | Main API endpoint `/analyze-speech` — runs entire pipeline | Calls `analyze_full()` for analysis, `generate_response()` for LLM output, `synthesize_speech()` for TTS output |

### `app/services`

| `.py` File | Main Functionality | Key Drivers (How functionality is achieved) |
| ----- | ----- | ----- |
| **`speech_ProcessingPipeline.py`** | End-to-end speech analysis pipeline | Integrates `speech_EmotionRecognition`, `speech_Transcription`, `speech_SentimentAnalysis` modules → runs sequentially on input `.wav` |
| **`speech_EmotionRecognition.py`** | Recognizes **speech emotion** from audio | Loads `superb/wav2vec2-base-superb-er` via Transformers → performs emotion classification with confidence |
| **`speech_Transcription.py`** | Transcribes audio → text and detects language | Uses `voidful/wav2vec2-xlsr-multilingual-56` (or Whisper fallback) via HuggingFace pipeline → outputs transcript and language |
| **`speech_SentimentAnalysis.py`** | Analyzes **sentiment** of transcribed text | Uses `cardiffnlp/twitter-xlm-roberta-base-sentiment` model via Transformers pipeline → outputs sentiment + confidence |
| **`speech_DialogueManager.py`** | Generates final **empathetic text response** | Calls **DeepSeek API** (`https://api.deepseek.com/v1/chat/completions`) → constructs prompt using `analysis_result` → retrieves assistant reply |
| **`speech_SpeechSynthesis.py`** | Converts **response text → speech audio (MP3)** | Uses `gTTS` (Google Text-to-Speech Python lib) → supports `en`, `id`, `ms` languages → saves output as MP3 to `/data/tts_output/` |