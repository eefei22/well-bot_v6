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
  - `speech_EmotionRecognition` → classify emotion from audio.
  - `speech_Transcription` → transcribe speech to text and detect language.
  - `speech_SentimentAnalysis` → analyze sentiment of the transcript.

### `speech_DialogueManager.py`
- Generates a warm and supportive response using the **DeepSeek API** (LLM chat API).
- Constructs a chat prompt based on emotion, sentiment, and transcript.
- Returns the generated response text.

### `speech_SpeechSynthesis.py`
- Converts the generated response text to an MP3 audio file using **gTTS** (Google Text-to-Speech).
- Automatically selects language based on detected speech language.
- Returns the path to the generated audio file.

### `speech_EmotionRecognition.py`
- Uses **wav2vec2-based emotion classifier** (`superb/wav2vec2-base-superb-er`) to classify emotion from the uploaded `.wav` audio.

### `speech_Transcription.py`
- Transcribes speech to text and detects language.
- Currently uses `voidful/wav2vec2-xlsr-multilingual-56` or **Whisper** fallback.
- Returns transcript text and detected language.

### `speech_SentimentAnalysis.py`
- Analyzes sentiment of the transcript using **XLM-RoBERTa-based sentiment model** (`cardiffnlp/twitter-xlm-roberta-base-sentiment`).
- Returns sentiment label and confidence.

# Models Used
## Emotion Recognition
- **Model**: `superb/wav2vec2-base-superb-er`
- **Framework**: HuggingFace Transformers
- **Purpose**: Classify speech emotion with confidence.

## Transcription
- **Model**: `voidful/wav2vec2-xlsr-multilingual-56` (planned) or **Whisper** fallback.
- **Framework**: HuggingFace Transformers
- **Purpose**: Transcribe audio to text and detect language.

## Sentiment Analysis
- **Model**: `cardiffnlp/twitter-xlm-roberta-base-sentiment`
- **Framework**: HuggingFace Transformers
- **Purpose**: Classify sentiment polarity of transcript text.

## Dialogue Manager
- **Model**: DeepSeek API → `deepseek-chat`
- **Framework**: External API (OpenAI-compatible)
- **Purpose**: Generate warm and supportive responses based on emotion, sentiment, and transcript.

## Speech Synthesis
- **Model**: `gTTS` (Google Text-to-Speech)
- **Framework**: gTTS Python library
- **Purpose**: Convert generated response text to speech (MP3), supports `en`, `id`, `ms`.

## Sample API Response

Example JSON returned by `/analyze-speech` endpoint:

```json
{
  "analysis_result": {
    "emotion": "ang",
    "emotion_confidence": 0.5964024066925049,
    "transcript": " Ini satu lagi perangai tak elok.",
    "language": "id",
    "sentiment": "negative",
    "sentiment_confidence": 0.8975903987884521
  },
  "generated_response": "I hear the frustration in your words, and I want you to know that your feelings are completely valid. It sounds like you're dealing with something really challenging right now. Would you like to talk more about what's bothering you? I'm here to listen and support you in any way I can. Remember, it's okay to feel upset—you're not alone in this.",
  "tts_audio_path": "data/tts_output/tts_output_xxxxxxxxxxxxxxxx.mp3"
}
