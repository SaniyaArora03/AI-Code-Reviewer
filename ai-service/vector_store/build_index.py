import os
import sys

import joblib
import numpy as np
import pandas as pd


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from embeddings.codebert_embedder import CodeBERTEmbedder


print("Loading dataset...")

df = pd.read_csv("../data/dataset.csv")


df = df.sample(1000, random_state=42)

print(f"Loaded {len(df)} samples")

print("Loading CodeBERT...")
embedder = CodeBERTEmbedder()
print("CodeBERT loaded!")

import faiss
embeddings = []

print("Generating embeddings...")

for idx, code in enumerate(df["func"]):

    vector = embedder.get_embedding(str(code))

    embeddings.append(vector)

    if idx % 100 == 0:
        print(f"Processed {idx}")

embeddings = np.array(embeddings).astype("float32")

print("\nEmbedding Shape:")
print(embeddings.shape)


dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension) #euclidean distance

index.add(embeddings)

print(f"\nVectors stored: {index.ntotal}")


faiss.write_index(index, "faiss.index")


metadata = []

for _, row in df.iterrows():

    metadata.append(
        {
            "code": row["func"],
            "label": bool(row["target"])
        }
    )

joblib.dump(metadata, "metadata.pkl")

print("\nFAISS index saved!")
print("Metadata saved!")