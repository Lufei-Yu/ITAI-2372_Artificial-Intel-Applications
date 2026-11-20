# 📚 Smart Study Guide & Practice Quiz Generator

An AI-powered study application that turns lecture notes and text-based PDFs into structured summaries, flashcards, and multiple-choice quizzes with answer explanations.

## Features

- Upload a text-based PDF or paste notes directly.
- Extract text from PDF documents.
- Generate structured study summaries.
- Generate question-and-answer flashcards.
- Create multiple-choice quizzes with four options.
- Explain why each option is correct or incorrect.
- Recommend the next quiz difficulty based on the latest score.

## Technology stack

- Python
- Streamlit
- OpenAI API (Responses API with structured outputs)
- PyPDF2
- Pydantic
- python-dotenv

## Project structure

```text
Smart-Study-Guide-Quiz-Generator/
├── app.py
├── ai_engine.py
├── pdf_processor.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
└── generated/
```

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

This project demonstrates Generative AI integration, prompt engineering, structured LLM outputs, document processing, Python development, and interactive application design.
