import os
import sys

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from rag.pipeline import ReviewPipeline


app = FastAPI(
    title="AI Code Reviewer",
    version="1.0.0"
)

print("Starting AI Pipeline...")

pipeline = ReviewPipeline()

print("Pipeline Loaded!")



class CodeRequest(BaseModel):
    code: str



@app.get("/")
def home():

    return {
        "message": "AI Code Reviewer API Running"
    }



@app.post("/review")
def review_code(request: CodeRequest):
    

    result = pipeline.review(
        request.code
    )

    return result

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)