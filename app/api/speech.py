# app/api/speech.py

from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
import tempfile
import shutil
from app.services.speech_Pipeline import analyze_full

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

    # Run full pipeline
    result = analyze_full(tmp_path)

    return result
