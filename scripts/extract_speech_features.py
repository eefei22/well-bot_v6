# scripts/extract_speech_features.py

import os
import opensmile
import pandas as pd
from tqdm import tqdm

# ============================
# 🔧 openSMILE setup
# ============================

smile = opensmile.Smile(
    feature_set=opensmile.FeatureSet.ComParE_2016,
    feature_level=opensmile.FeatureLevel.Functionals
)

# ============================
# 📚 RAVDESS parser
# ============================

RAVDESS_EMOTION_MAP = {
    "01": "neutral",
    "02": "calm",
    "03": "happy",
    "04": "sad",
    "05": "angry",
    "06": "fearful",
    "07": "disgust",
    "08": "surprised"
}

def parse_ravdess_label(filename):
    parts = filename.split("-")
    if len(parts) > 2:
        return RAVDESS_EMOTION_MAP.get(parts[2], "unknown")
    return "unknown"

# ============================
# 📚 CREMA-D parser
# ============================

CREMA_EMOTION_MAP = {
    'ANG': 'angry',
    'DIS': 'disgust',
    'FEA': 'fearful',
    'HAP': 'happy',
    'NEU': 'neutral',
    'SAD': 'sad'
}

def parse_crema_label(filename):
    code = filename.split("_")[2]
    return CREMA_EMOTION_MAP.get(code, "unknown")

# ============================
# 📚 TESS parser
# ============================

def parse_tess_label(foldername):
    return foldername.lower().replace("pleasant_surprise", "surprised")

# ============================
# 🚀 Feature Extraction Logic
# ============================

def extract_dataset(dataset_name, base_path, label_func, recursive=False):
    """
    Generic extraction for any dataset.
    Args:
        dataset_name: str, name used for dataset column
        base_path: str, path to folder
        label_func: callable, extracts emotion label
        recursive: bool, whether to traverse subdirs
    Returns:
        DataFrame
    """
    rows = []
    for root, _, files in os.walk(base_path):
        for file in tqdm(files, desc=f"Processing {dataset_name}"):
            if file.endswith(".wav"):
                full_path = os.path.join(root, file)
                try:
                    features = smile.process_file(full_path)
                    label = label_func(file if not recursive else root.split(os.sep)[-1])
                    features["emotion"] = label
                    features["source"] = dataset_name
                    features["file"] = file
                    rows.append(features)
                except Exception as e:
                    print(f"❌ Skipping {file}: {e}")
    if rows:
        return pd.concat(rows)
    return pd.DataFrame()

# ============================
# 🧠 Main
# ============================

if __name__ == "__main__":
    datasets = []

    # RAVDESS
    datasets.append(extract_dataset(
        dataset_name="ravdess",
        base_path="data/audio_raw/ravdess",
        label_func=parse_ravdess_label
    ))

    # CREMA-D
    datasets.append(extract_dataset(
        dataset_name="crema",
        base_path="data/audio_raw/crema",
        label_func=parse_crema_label
    ))

    # TESS
    datasets.append(extract_dataset(
        dataset_name="tess",
        base_path="data/audio_raw/tess",
        label_func=parse_tess_label,
        recursive=True  # folder name = emotion
    ))

    # Combine and export
    all_data = pd.concat(datasets, ignore_index=True)
    os.makedirs("data/features", exist_ok=True)
    output_path = "data/features/emotion_features.csv"
    all_data.to_csv(output_path, index=False)
    print(f"\n✅ Feature extraction complete. CSV saved to: {output_path}")
