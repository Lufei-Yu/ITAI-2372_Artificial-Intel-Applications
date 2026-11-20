import os
from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel, Field

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
MODEL = os.getenv("OPENAI_MODEL", "gpt-4o")

if not API_KEY:
    raise RuntimeError(
        "OPENAI_API_KEY is missing. Add it to your .env file before starting the app."
    )

client = OpenAI(api_key=API_KEY)


class Summary(BaseModel):
    title: str
    overview: str
    key_concepts: list[str]
    important_terms: list[str]
    study_tips: list[str]


class Flashcard(BaseModel):
    question: str
    answer: str


class FlashcardSet(BaseModel):
    flashcards: list[Flashcard]


class QuizQuestion(BaseModel):
    question: str
    options: list[str] = Field(min_length=4, max_length=4)
    correct_answer: str
    explanation: str
    option_explanations: list[str] = Field(min_length=4, max_length=4)
    difficulty: str


class QuizSet(BaseModel):
    questions: list[QuizQuestion]


def generate_structured_output(source_text: str, instructions: str, output_model):
    if not source_text or len(source_text.strip()) < 50:
        raise ValueError("Please provide at least 50 characters of study material.")

    # Starter-project safeguard. For long documents, add chunking/retrieval.
    source_text = source_text[:30000]

    response = client.responses.parse(
        model=MODEL,
        input=[
            {
                "role": "system",
                "content": (
                    "You are an expert study assistant. Use only the supplied study "
                    "material. Do not invent facts. If the source is unclear, state "
                    "that uncertainty. Produce accurate, student-friendly content."
                ),
            },
            {
                "role": "user",
                "content": f"{instructions}\n\nSTUDY MATERIAL:\n{source_text}",
            },
        ],
        text_format=output_model,
    )

    parsed = response.output_parsed
    if parsed is None:
        raise ValueError("The model did not return a valid structured response.")
    return parsed


def generate_summary(text: str) -> Summary:
    instructions = """
Create a structured study guide containing:
- A concise, meaningful title.
- A clear overview of the supplied material.
- The most important key concepts.
- Important terms with brief definitions.
- Practical study tips based on the material.
Make it organized and easy for a student to understand.
"""
    return generate_structured_output(text, instructions, Summary)


def generate_flashcards(text: str, number: int = 10) -> FlashcardSet:
    number = max(1, min(int(number), 30))
    instructions = f"""
Generate exactly {number} useful flashcards from the supplied material.
Each card needs one clear question and a concise, accurate answer.
Cover different important concepts and avoid duplicates.
"""
    result = generate_structured_output(text, instructions, FlashcardSet)
    if len(result.flashcards) != number:
        raise ValueError(
            f"Requested {number} flashcards, but the model returned "
            f"{len(result.flashcards)}. Please try again."
        )
    return result


def generate_quiz(text: str, number: int = 5, difficulty: str = "Medium") -> QuizSet:
    number = max(1, min(int(number), 15))
    if difficulty not in {"Easy", "Medium", "Hard"}:
        difficulty = "Medium"

    instructions = f"""
Generate exactly {number} multiple-choice questions at {difficulty} difficulty.
For every question:
1. Provide exactly four distinct answer options.
2. Set correct_answer to the exact text of one option.
3. Explain why the correct answer is correct.
4. Provide exactly four option_explanations, aligned with the options in order.
5. Explain why each incorrect option is incorrect.
6. Cover different concepts and avoid ambiguous questions.
7. Set difficulty to {difficulty}.
"""
    result = generate_structured_output(text, instructions, QuizSet)

    if len(result.questions) != number:
        raise ValueError(
            f"Requested {number} questions, but the model returned "
            f"{len(result.questions)}. Please try again."
        )

    for question in result.questions:
        if len(question.options) != 4:
            raise ValueError("Every quiz question must have four options.")
        if question.correct_answer not in question.options:
            raise ValueError("The correct answer must exactly match an option.")
        if len(question.option_explanations) != 4:
            raise ValueError("Every option must have an explanation.")

    return result


def get_next_difficulty(score: int) -> str:
    if score >= 80:
        return "Hard"
    if score >= 50:
        return "Medium"
    return "Easy"
