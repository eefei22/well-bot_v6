# app/services/speech_DialogueManager.py

import os
import requests
from dotenv import load_dotenv
load_dotenv()  # Load .env file

# DeepSeek key and URL
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
DEEPSEEK_API_URL = "https://api.deepseek.com/v1/chat/completions"

# === Prompt Template ===
SYSTEM_PROMPT = """You are Well-Bot, a friendly and empathetic emotional support robot. You respond to users based on detected emotions and speech, helping them feel heard and supported."""

USER_PROMPT_TEMPLATE = """
Provide a friendly and empathetic response to the user based on the following analysis:

Transcript: "{transcript}"
Emotion detected: {emotion}
Sentiment detected: {sentiment}
"""

def generate_response(analysis_payload: dict, extra_prompt: str = "") -> str:
    if not DEEPSEEK_API_KEY:
        raise RuntimeError("DEEPSEEK_API_KEY not set in environment variables.")

    user_message = USER_PROMPT_TEMPLATE.format(
        transcript=analysis_payload.get('transcript', ''),
        emotion=analysis_payload.get('emotion', 'unknown'),
        sentiment=analysis_payload.get('sentiment', 'unknown'),
        extra_prompt=extra_prompt
    )

    # Build chat messages
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_message},
    ]

    # Build payload
    payload = {
        "model": "deepseek-chat",
        "messages": messages,
        "max_tokens": 512,
        "temperature": 0.8,
        "top_p": 0.85
    }

    # Send request to DeepSeek API
    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.post(DEEPSEEK_API_URL, json=payload, headers=headers)
    response.raise_for_status()

    response_data = response.json()
    reply_text = response_data["choices"][0]["message"]["content"].strip()

    return reply_text
