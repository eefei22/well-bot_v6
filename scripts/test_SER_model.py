# scripts/test_SER_model.py

import os
import joblib
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app.services.speech_emo_analysis import SpeechEmotionAnalyzer

def main():
    test_file = "data/audio_samples/speech_tester4.wav"
    print(f"🎧 Testing file: {test_file}")

    analyzer = SpeechEmotionAnalyzer()
    result = analyzer.predict_emotion(test_file)

    print("🧪 Raw result from model:", result)  # <-- This is important

    if "error" in result:
        print("❌ Error during prediction:", result["error"])
    else:
        print("\n=== Emotion Prediction ===")
        print("Predicted Emotion :", result["emotion"])
        print("Confidence         :", result["confidence"])
        print("All Probabilities  :", result["probabilities"])

if __name__ == "__main__":
    main()
