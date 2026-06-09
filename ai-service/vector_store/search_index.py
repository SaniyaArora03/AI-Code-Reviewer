import os
import sys
from pathlib import Path

import joblib
import numpy as np
import faiss

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from embeddings.codebert_embedder import CodeBERTEmbedder


class SimilaritySearcher:

    def __init__(self):

        print("Loading CodeBERT...")
        self.embedder = CodeBERTEmbedder()
        print("CodeBERT loaded!")

        BASE_DIR = Path(__file__).resolve().parent

        index_path = BASE_DIR / "faiss.index"
        metadata_path = BASE_DIR / "metadata.pkl"

        print("Loading FAISS index...")
        print("Index Path:", index_path)

        self.index = faiss.read_index(
            str(index_path)
        )

        self.metadata = joblib.load(
            metadata_path
        )

        print("FAISS loaded!")

    def search(self, code, k=5):

        query_vector = self.embedder.get_embedding(
            code
        )

        query_vector = np.array(
            [query_vector],
            dtype="float32"
        )

        distances, indices = self.index.search(
            query_vector,
            k
        )

        results = []

        for idx in indices[0]:

            results.append(
                self.metadata[idx]
            )

        return results


if __name__ == "__main__":

    sample_code = """
def divide(a,b):
    return a/b
"""

    searcher = SimilaritySearcher()

    results = searcher.search(
        sample_code
    )

    print("\nTop Similar Examples:\n")

    for i, item in enumerate(results):

        print(f"\nExample {i+1}")
        print("Label:", item["label"])
        print(item["code"][:300])