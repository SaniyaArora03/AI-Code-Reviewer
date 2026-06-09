from transformers import AutoTokenizer, AutoModel
import torch


class CodeBERTEmbedder:

    def __init__(self):

        self.tokenizer = AutoTokenizer.from_pretrained(
            "microsoft/codebert-base"
        )

        self.model = AutoModel.from_pretrained(
            "microsoft/codebert-base"
        )

    def get_embedding(self, code):

        inputs = self.tokenizer(
            code,
            return_tensors="pt",
            truncation=True,
            max_length=512,
            padding=True
        )

        with torch.no_grad():

            outputs = self.model(**inputs)

        embedding = outputs.last_hidden_state[:, 0, :]

        return embedding.squeeze().numpy()


if __name__ == "__main__":

    sample_code = """
def divide(a,b):
    return a/b
"""

    embedder = CodeBERTEmbedder()

    vector = embedder.get_embedding(sample_code)

    print("Embedding Shape:")
    print(vector.shape)