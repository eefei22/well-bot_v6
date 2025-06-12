# app/services/speech_SpeechSynthesis.py

import os
import uuid
from gtts import gTTS

# Output directory
TTS_OUTPUT_DIR = "data/tts_output"
os.makedirs(TTS_OUTPUT_DIR, exist_ok=True)

# Map from detected language to gTTS supported language codes
LANGUAGE_MAP = {
    "id": "id", 
    "ms": "ms", 
    "en": "en",
    "unknown": "en"
}

def synthesize_speech(text: str, detected_language: str = "unknown", output_filename: str = None) -> str:
    print(f"[TTS] Synthesizing: {text}")

    # Pick language code
    lang_code = LANGUAGE_MAP.get(detected_language, "en")

    # Generate unique filename if not provided
    if not output_filename:
        output_filename = f"tts_output_{uuid.uuid4().hex}.mp3"

    audio_path = os.path.join(TTS_OUTPUT_DIR, output_filename)

    # Synthesize speech
    tts = gTTS(text=text, lang=lang_code)
    tts.save(audio_path)

    print(f"[TTS] Saved audio to: {audio_path}")
    return audio_path
