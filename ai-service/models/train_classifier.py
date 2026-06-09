import pandas as pd
import numpy as np
import joblib

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from embeddings.codebert_embedder import CodeBERTEmbedder


print("Loading dataset...")

df = pd.read_csv("../data/dataset.csv")

df = df[["func", "target"]]

# Use 10 initially for testing
df = df.sample(1000, random_state=42)

print(f"Using {len(df)} samples")

print("Loading CodeBERT...")
embedder = CodeBERTEmbedder()
print("CodeBERT loaded!")

embeddings = []

for idx, code in enumerate(df["func"]):

    print(f"Processing sample {idx}")

    vector = embedder.get_embedding(str(code))

    embeddings.append(vector)

print("All embeddings generated!")

X = np.array(embeddings)

y = df["target"].astype(int)

print("Embedding Shape:", X.shape)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Training Random Forest...")

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print(f"Accuracy: {accuracy:.4f}")

joblib.dump(model, "random_forest_model.pkl")

print("Model saved!")