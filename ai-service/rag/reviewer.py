import os
import requests
from dotenv import load_dotenv

load_dotenv()


class CodeReviewer:

    def __init__(self):

        self.api_key = os.getenv("OPENROUTER_API_KEY")

        if not self.api_key:
            raise ValueError(
                "OPENROUTER_API_KEY not found in .env"
            )

        self.url = "https://openrouter.ai/api/v1/chat/completions"

        # Good coding model
        self.model = "deepseek/deepseek-chat-v3"

        print("Reviewer initialized!")

    def build_prompt(
        self,
        user_code,
        prediction,
        similar_examples
    ):

        examples_text = ""

        for idx, example in enumerate(similar_examples, start=1):

            examples_text += f"""
Example {idx}

Label:
{example['label']}

Code:
{example['code'][:400]}

----------------------------------------
"""

        prompt = f"""
You are a senior software engineer.

Review the code below.

=========================
USER CODE
=========================

{user_code}

=========================
CLASSIFIER RESULT
=========================

{prediction}

=========================
SIMILAR EXAMPLES
=========================

{examples_text}

=========================
TASK
=========================

Provide:

1. Issue Summary
2. Root Cause
3. Severity (Low/Medium/High)
4. Suggested Improvements
5. Corrected Code
6. Best Practices

Return detailed technical explanations.
"""

        return prompt

    def review_code(
        self,
        user_code,
        prediction,
        similar_examples
    ):

        prompt = self.build_prompt(
            user_code,
            prediction,
            similar_examples
        )

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": self.model,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "temperature": 0.2,
            "max_tokens": 800
        }

        response = requests.post(
            self.url,
            headers=headers,
            json=payload
        )

        response.raise_for_status()

        result = response.json()

        return result["choices"][0]["message"]["content"]


if __name__ == "__main__":

    sample_code = """
def divide(a,b):
    return a/b
"""

    prediction = "Defective"

    similar_examples = [
        {
            "label": True,
            "code": """
def divide(x,y):
    return x/y
"""
        },
        {
            "label": True,
            "code": """
result = numerator/denominator
"""
        }
    ]

    reviewer = CodeReviewer()

    review = reviewer.review_code(
        sample_code,
        prediction,
        similar_examples
    )

    print("\n" + "=" * 80)
    print("AI REVIEW")
    print("=" * 80)
    print(review)