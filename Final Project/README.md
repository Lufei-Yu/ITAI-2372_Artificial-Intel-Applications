#  Smart Study Guide & Practice Quiz Generator

## Project Overview

The Smart Study Guide & Practice Quiz Generator is an AI-powered educational application designed to help students improve their learning efficiency, knowledge retention, and exam preparation through intelligent study material generation.

Traditional studying often involves reviewing lengthy lecture notes, textbook chapters, academic articles, and PDF documents. This process can be time-consuming and inefficient, especially when students need to identify important concepts, understand complex topics, and prepare for examinations.

This project addresses these challenges by integrating Generative Artificial Intelligence (GenAI), Natural Language Processing (NLP), and Large Language Models (LLMs) into an interactive study platform. The application transforms unstructured educational content into organized, personalized, and interactive learning resources.

Students can upload course materials in PDF format or paste their lecture notes directly into the application. The AI engine processes the provided content and generates structured study summaries, question-and-answer flashcards, and multiple-choice practice quizzes. Each quiz includes detailed explanations that help students understand why an answer is correct and why alternative answers are incorrect.

The application also incorporates an adaptive learning mechanism that evaluates quiz performance and recommends an appropriate difficulty level for subsequent practice sessions. This encourages students to progressively strengthen their understanding and focus on areas that require additional review.

## Features

- Upload a text-based PDF or paste notes directly.
- Extract text from PDF documents.
- Generate structured study summaries.
- Generate question-and-answer flashcards.
- Create multiple-choice quizzes with four options.
- Explain why each option is correct or incorrect.
- Recommend the next quiz difficulty based on the latest score.

## Technology stack

| Technology | Application |
|---|---|
| Python | Core application development and processing logic |
| Streamlit | Interactive web-based user interface |
| OpenAI API | Large Language Model integration and content generation |
| PyPDF2 | PDF document text extraction |
| Pydantic | Structured output validation and data modeling |
| python-dotenv | Secure API key configuration |
| Generative AI | Automated summaries, flashcards, and quiz generation |
| Natural Language Processing | Understanding and transforming educational text |


## Setup

### 1. Create and activate a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure your API key

Copy `.env.example` to `.env` and replace the placeholder with your OpenAI API key:

```env
OPENAI_API_KEY=your_actual_api_key
OPENAI_MODEL=gpt-4o
```

Keep `.env` private. Never commit your API key to GitHub.

### 4. Start the app

```bash
streamlit run app.py
```

Open the local URL printed in your terminal (usually `http://localhost:8501`).

## How to use

1. Upload a text-based PDF and click **Extract PDF text**, or paste notes into the text area.
2. Choose the number of flashcards and quiz questions in the sidebar.
3. Generate a summary, flashcards, or quiz.
4. Submit all quiz answers to see your score and explanations.
5. Use the recommended difficulty for your next practice quiz.

## Important limitations

- This starter version extracts selectable text. Scanned PDFs need OCR, which is not included.
- The AI input is capped at 30,000 characters per request. Long-document chunking and retrieval are future improvements.
- Adaptive difficulty uses the most recent quiz score; it is not yet a long-term learner model.
- API calls require internet access and may incur OpenAI API charges.
- Generated study materials should be checked against the original course material.

## Future improvements

- OCR for scanned documents.
- Long-document chunking and retrieval.
- Persistent student accounts and quiz history with SQLite.
- Spaced-repetition scheduling for flashcards.
- Export study guides and quiz results to PDF.
- Course and subject organization.
- Deployment to Streamlit Community Cloud.

## Learning outcomes

- Gained hands-on experience building an AI-powered study application using Python.
- Learned to integrate the OpenAI API for AI-generated summaries, flashcards, and quizzes.
- Developed skills in PDF text extraction and document processing.
- Practiced using structured data models with Pydantic.
- Improved understanding of Natural Language Processing (NLP) and Generative AI.
- Learned to build interactive web applications using Streamlit.
- Explored adaptive learning techniques to personalize quiz difficulty based on user performance.
