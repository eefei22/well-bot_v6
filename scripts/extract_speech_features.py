import os
import librosa
import numpy as np
import pandas as pd
from tqdm import tqdm

# ============================
# 📚 Dataset Label Parsers
# ============================

RAVDESS_EMOTION_MAP = {
    "01": "neutral", "02": "calm", "03": "happy", "04": "sad",
    "05": "angry", "06": "fearful", "07": "disgust", "08": "surprised"
}

CREMA_EMOTION_MAP = {
    'ANG': 'angry', 'DIS': 'disgust', 'FEA': 'fearful',
    'HAP': 'happy', 'NEU': 'neutral', 'SAD': 'sad'
}

VALID_EMOTIONS = {
    'angry', 'calm', 'disgust', 'fearful',
    'happy', 'neutral', 'sad', 'surprised'
}

def parse_ravdess_label(filename):
    parts = filename.split("-")
    return RAVDESS_EMOTION_MAP.get(parts[2], "unknown") if len(parts) > 2 else "unknown"

def parse_crema_label(filename):
    code = filename.split("_")[2]
    return CREMA_EMOTION_MAP.get(code, "unknown")

def parse_tess_label(filename):
    parts = filename.lower().split("_")
    if parts[-1].endswith(".wav"):
        emotion = parts[-1].replace(".wav", "")
        emotion = "surprised" if emotion == "ps" else emotion
        return emotion if emotion in VALID_EMOTIONS else "unknown"
    return "unknown"

# ============================
# 🚀 Librosa Feature Extractor
# ============================

def extract_librosa_features(file_path):
    y, sr = librosa.load(file_path, sr=None)
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    zcr = librosa.feature.zero_crossing_rate(y)
    rmse = librosa.feature.rms(y=y)

    features = np.concatenate([
        np.mean(mfccs, axis=1),
        np.mean(zcr, axis=1),
        np.mean(rmse, axis=1)
    ])
    return features

# ============================
# Generic Extraction Logic
# ============================

def extract_dataset(dataset_name, base_path, label_func, recursive=False):
    rows = []
    for root, _, files in os.walk(base_path):
        for file in tqdm(files, desc=f"Processing {dataset_name}"):
            if file.endswith(".wav"):
                full_path = os.path.join(root, file)
                try:
                    label = label_func(file if not recursive else root.split(os.sep)[-1])
                    if label == "unknown":
                        continue  # skip bad labels
                    features = extract_librosa_features(full_path)
                    rows.append({
                        **{f'f{i+1}': feat for i, feat in enumerate(features)},
                        "emotion": label,
                        "source": dataset_name,
                        "file": file
                    })
                except Exception as e:
                    print(f"❌ Skipping {file}: {e}")
    return pd.DataFrame(rows)

# ============================
# 🧠 Main
# ============================

if __name__ == "__main__":
    datasets = [
        extract_dataset("ravdess", "data/audio_raw/ravdess", parse_ravdess_label),
        extract_dataset("crema", "data/audio_raw/crema", parse_crema_label),
        extract_dataset("tess", "data/audio_raw/tess", parse_tess_label, recursive=False)
    ]

    all_data = pd.concat(datasets, ignore_index=True)
    os.makedirs("data/features", exist_ok=True)
    output_path = "data/features/emotion_features.csv"
    all_data.to_csv(output_path, index=False)
    print(f"\n✅ Feature extraction complete. CSV saved to: {output_path}")
