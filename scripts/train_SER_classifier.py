# scripts/train_SER_classifier.py

import pandas as pd
import numpy as np
import os
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline
from sklearn.metrics import classification_report, confusion_matrix
import joblib
import threading
import time

# ========== Heartbeat Logger ==========

def heartbeat(interval=300):  # 300 seconds = 5 minutes
    while True:
        time.sleep(interval)
        print(f"🕒 Still training... [{time.strftime('%H:%M:%S')}]")

# Start logger thread before training
logger_thread = threading.Thread(target=heartbeat, daemon=True)
logger_thread.start()


# ==========
# 📥 Load features
# ==========

df = pd.read_csv("data/features/emotion_features.csv")

# 🔍 Check for invalid labels before training
print("🚨 Detected emotion labels:", df["emotion"].unique())
valid_emotions = ['angry', 'calm', 'disgust', 'fearful', 'happy', 'neutral', 'sad', 'surprised']
df = df[df["emotion"].isin(valid_emotions)]



# Drop non-feature columns
X = df.drop(columns=["emotion", "source", "file"])
y = df["emotion"]

# ==========
# 🔢 Encode labels
# ==========

label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# ==========
# 📊 Train/test split
# ==========

X_train, X_test, y_train, y_test = train_test_split(
    X, y_encoded, test_size=0.2, stratify=y_encoded, random_state=42
)

# ==========
# 🧠 Train classifier
# ==========

clf = make_pipeline(
    StandardScaler(),
    SVC(kernel="rbf", probability=True, class_weight="balanced")
)

print("🚀 Training started...")
logger_thread = threading.Thread(target=heartbeat, daemon=True)
logger_thread.start()
clf.fit(X_train, y_train)


clf.fit(X_train, y_train)

# ==========
# 📈 Evaluate
# ==========

y_pred = clf.predict(X_test)
print("\n🔍 Classification Report:")
print(classification_report(y_test, y_pred, target_names=label_encoder.classes_))

# Optional: Show confusion matrix
# print(confusion_matrix(y_test, y_pred))

# ==========
# 💾 Save model
# ==========

output_path = "app/services/SER_model.pkl"
joblib.dump({
    "classifier": clf,
    "label_encoder": label_encoder
}, output_path)

print(f"\n✅ Model trained and saved to: {output_path}")
