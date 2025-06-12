# app/api/speech.py

from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
import tempfile
import shutil

from app.services.speech_ProcessingPipeline import analyze_full
from app.services.speech_DialogueManager import generate_response
from app.services.speech_SpeechSynthesis import synthesize_speech

router = APIRouter()

@router.post("/analyze-speech")
async def analyze_speech(file: UploadFile = File(...)):
    if not file.filename.endswith(".wav"):
        return JSONResponse(status_code=400, content={"error": "Only .wav files are supported."})

    # Save uploaded file to a temp file
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
            shutil.copyfileobj(file.file, tmp)
            tmp_path = tmp.name
    finally:
        file.file.close()

    # Analyse Speech
    analysis_result = analyze_full(tmp_path)

    # Generate response
    response_text = generate_response(analysis_result, extra_prompt="Keep the tone warm and supportive.")
    tts_audio_path = synthesize_speech(response_text)

    # Return combined result:
    return {
        "analysis_result": analysis_result,
        "generated_response": response_text,
        "tts_audio_path": tts_audio_path
    }

