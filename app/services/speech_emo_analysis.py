import os
import opensmile
import numpy as np
import joblib

class SpeechEmotionAnalyzer:
    def __init__(self):
        self.smile = opensmile.Smile(
            feature_set=opensmile.FeatureSet.ComParE_2016,
            feature_level=opensmile.FeatureLevel.Functionals
        )

        # Load the trained model
        model_path = os.path.join(os.path.dirname(__file__), 'SER_model.pkl')
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"❌ Model file not found at {model_path}")
        
        model_data = joblib.load(model_path)
        self.model = model_data['classifier']
        self.label_encoder = model_data['label_encoder']

    def extract_features(self, file_path: str) -> np.ndarray:
        features_df = self.smile.process_file(file_path)
        return features_df.iloc[0].values.reshape(1, -1)

    def predict_emotion(self, file_path: str) -> dict:
        try:
            features = self.extract_features(file_path)
            probabilities = self.model.predict_proba(features)[0]
            top_idx = np.argmax(probabilities)
            predicted_label = self.label_encoder.inverse_transform([top_idx])[0]

            return {
                "emotion": predicted_label,
                "confidence": float(probabilities[top_idx]),
                "probabilities": dict(zip(self.label_encoder.classes_, probabilities.round(4)))
            }

        except Exception as e:
            return {"error": str(e)}
