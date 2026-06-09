AI Code Reviewer
Overview

An intelligent code review platform that combines Machine Learning, Code Embeddings, Retrieval-Augmented Generation (RAG), and Large Language Models to automatically analyze source code, detect potential defects, retrieve similar bug patterns, and generate detailed code review reports with suggested fixes.

Features
Automated code quality analysis
Defect prediction using Machine Learning
Code embeddings using CodeBERT
Similar bug retrieval using FAISS
AI-generated review reports
Suggested fixes and best practices
FastAPI backend
React frontend
REST API integration

Architecture
User Code
    │
    ▼
CodeBERT
    │
    ▼
Embedding Vector
    │
    ├─────────────► Random Forest
    │                    │
    │                    ▼
    │             Defect Prediction
    │
    ▼
FAISS Vector Search
    │
    ▼
Similar Bug Examples
    │
    ▼
Prompt Construction
    │
    ▼
DeepSeek LLM (OpenRouter)
    │
    ▼
AI Review Report

Tech Stack
Machine Learning
-Scikit-Learn
-Random Forest
Deep Learning
-Hugging Face Transformers
-Microsoft CodeBERT
Retrieval
-FAISS
LLM
-DeepSeek V3
-OpenRouter API
Backend
-FastAPI
-Uvicorn
Frontend
-React
-Axios
Dataset
-CodeXGLUE Defect Detection Dataset

Workflow
Step 1: Dataset Preparation

The CodeXGLUE Defect Detection dataset is downloaded and converted into a structured dataset suitable for model training.

Step 2: Embedding Generation

Code snippets are converted into dense vector representations using Microsoft's CodeBERT model.

Step 3: Defect Prediction

A Random Forest classifier predicts whether a submitted code snippet is likely to contain defects.

Step 4: Similar Bug Retrieval

FAISS performs vector similarity search to retrieve code snippets that are semantically similar to the submitted code.

Step 5: AI Review Generation

The submitted code, classifier prediction, and retrieved examples are combined into a prompt and sent to DeepSeek via OpenRouter.

Step 6: Result Delivery

A detailed review report containing:

Issue Summary
Root Cause
Severity
Suggested Improvements
Corrected Code
Best Practices

is returned to the user.

Running the Backend
uvicorn backend.main:app --reload

Running the Frontend
cd frontend
npm run dev