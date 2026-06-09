import os
import sys
import joblib
import numpy as np
from pathlib import Path

# Project root import fix
sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from embeddings.codebert_embedder import CodeBERTEmbedder
from vector_store.search_index import SimilaritySearcher
from rag.reviewer import CodeReviewer


class ReviewPipeline:

    def __init__(self):

        print("Loading components...")

        BASE_DIR = Path(__file__).resolve().parent.parent

        model_path = BASE_DIR / "models" / "random_forest_model.pkl"

        print("Loading model from:")
        print(model_path)

        self.model = joblib.load(model_path)

        self.embedder = CodeBERTEmbedder()

        self.searcher = SimilaritySearcher()

        self.reviewer = CodeReviewer()

        print("Pipeline Ready!")

    def predict_bug(self, code):

        embedding = self.embedder.get_embedding(code)

        embedding = np.array(
            [embedding]
        )

        prediction = self.model.predict(
            embedding
        )[0]

        probability = self.model.predict_proba(
            embedding
        )[0]

        confidence = max(probability)

        if prediction == 1:
            label = "Defective"
        else:
            label = "Clean"

        return label, confidence

    def review(self, code):

        

        prediction, confidence = self.predict_bug(
            code
        )

        similar_examples = self.searcher.search(
            code,
            k=5
        )

      

        review_text = self.reviewer.review_code(
            user_code=code,
            prediction=f"{prediction} ({confidence:.2f})",
            similar_examples=similar_examples
        )

        return {
            "prediction": prediction,
            "confidence": round(
                confidence * 100,
                2
            ),
            "review": review_text
        }


if __name__ == "__main__":

    sample_code = """
def divide(a,b):
    return a/b
"""

    pipeline = ReviewPipeline()

    result = pipeline.review(
        sample_code
    )

    print("\n")
    print("=" * 80)
    print("PREDICTION")
    print("=" * 80)

    print(
        result["prediction"]
    )

    print(
        result["confidence"]
    )

    print("\n")
    print("=" * 80)
    print("AI REVIEW")
    print("=" * 80)

    print(
        result["review"]
    )