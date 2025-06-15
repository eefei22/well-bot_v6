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

# Core `.py` Files and Responsibilities
### `speech_ProcessingPipeline.py`
- Main driver for full audio analysis pipeline.
- Calls the following components in sequence:
    #### `speech_EmotionRecognition.py` → classify emotion from audio.
    - Uses **wav2vec2-based emotion classifier** (`superb/wav2vec2-base-superb-er`) to classify emotion from the uploaded `.wav` audio.

    #### `speech_Transcription.py` → transcribe speech to text and detect language.
    - Transcribes speech to text and detects language.
    - Currently uses `openai/whisper-small`.
    - Returns transcript text and detected language.

    #### `speech_SentimentAnalysis.py` → analyze sentiment of the transcript.
    - Analyzes sentiment of the transcript using **XLM-RoBERTa-based sentiment model** (`cardiffnlp/twitter-xlm-roberta-base-sentiment`).
    - Returns sentiment label and confidence.

### `speech_DialogueManager.py`
- Generates a warm and supportive response using the **DeepSeek API** (LLM chat API).
- Constructs a chat prompt based on emotion, sentiment, and transcript.
- Returns the generated response text.

### `speech_SpeechSynthesis.py`
- Converts the generated response text to an MP3 audio file using **gTTS** (Google Text-to-Speech).
- Automatically selects language based on detected speech language.
- Returns the path to the generated audio file.

# Models Used
### **Emotion Recognition**
- Model: `superb/wav2vec2-base-superb-er`
- Framework: HuggingFace Transformers
- Purpose: Classify speech emotion with confidence scores.

### **Transcription**
- Model: `openai/whisper-small`.
- Framework: HuggingFace Transformers
- Purpose: Transcribe audio to text and detect language.

### **Sentiment Analysis**
- Model: `cardiffnlp/twitter-xlm-roberta-base-sentiment`
- Framework: HuggingFace Transformers
- Purpose: Classify sentiment polarity of transcript text.

### **Dialogue Manager**
- Model: DeepSeek API → `deepseek-chat`
- Framework: External API (OpenAI-compatible)
- Purpose: Generate warm and supportive responses based on emotion, sentiment, and transcript.

### **Speech Synthesis**
- Model: `gTTS` (Google Text-to-Speech)
- Framework: gTTS Python library
- Purpose: Convert generated response text to speech (MP3), supports `en`, `id`, `ms`.

