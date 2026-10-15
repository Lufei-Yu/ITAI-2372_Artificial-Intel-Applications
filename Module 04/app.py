import os
import requests
from flask import Flask, render_template, request
from model_training import load_sentiment_pipeline, train_sentiment_model, clean_text

app = Flask(__name__)

DATA_PATH = "sample_data.csv"
MODEL_PATH = "sentiment_model.pkl"
VECTORIZER_PATH = "vectorizer.pkl"

# Train a small demonstration model automatically if model files do not exist.
if not (os.path.exists(MODEL_PATH) and os.path.exists(VECTORIZER_PATH)):
    train_sentiment_model(DATA_PATH, MODEL_PATH, VECTORIZER_PATH)

predict_sentiment = load_sentiment_pipeline(MODEL_PATH, VECTORIZER_PATH)

# Optional local LLM endpoint. Example for Ollama's generate API:
# LLM_API_URL=http://localhost:11434/api/generate
LLM_API_URL = os.getenv("LLM_API_URL", "http://localhost:11434/api/generate")
LLM_MODEL = os.getenv("LLM_MODEL", "llama3.2")


def local_summary(text, question=None):
    """Fallback response so the prototype still works without an LLM service."""
    sentences = [s.strip() for s in text.replace("\n", " ").split(".") if s.strip()]
    if question:
        keywords = [w.lower().strip(".,?!") for w in question.split() if len(w) > 3]
        matches = [s for s in sentences if any(k in s.lower() for k in keywords)]
        if matches:
            return "Possible answer based on matching text: " + ". ".join(matches[:2]) + "."
        return ("I could not find a direct answer in the provided text. "
                "Review the article for details relevant to your question.")
    if sentences:
        return " ".join(sentences[:3]) + ("." if not sentences[0].endswith(".") else "")
    return "Please enter some financial text to analyze."


def ask_local_llm(text, question=None):
    task = (
        "Answer the user's question using only the provided financial text. "
        "If the text does not contain the answer, say so. Keep the answer concise. "
        "This is informational only, not financial advice."
        if question else
        "Summarize the financial text in 2-4 concise sentences. Mention key developments "
        "and risks, and do not invent facts. This is informational only, not financial advice."
    )
    prompt = f"{task}\n\nFinancial text:\n{text}\n"
    if question:
        prompt += f"\nUser question: {question}\n"
    try:
        response = requests.post(
            LLM_API_URL,
            json={"model": LLM_MODEL, "prompt": prompt, "stream": False},
            timeout=20,
        )
        response.raise_for_status()
        data = response.json()
        # Ollama uses "response"; some compatible endpoints may use "summary" or "answer".
        answer = data.get("response") or data.get("summary") or data.get("answer")
        if answer:
            return answer.strip(), "Local LLM"
        return local_summary(text, question), "Fallback (LLM returned no answer)"
    except (requests.RequestException, ValueError):
        return local_summary(text, question), "Fallback (local LLM not connected)"


@app.route("/", methods=["GET", "POST"])
def index():
    user_text = ""
    question = ""
    sentiment = None
    summary = None
    answer = None
    llm_status = None
    cleaned_preview = None

    if request.method == "POST":
        user_text = request.form.get("user_text", "").strip()
        question = request.form.get("question", "").strip()

        if user_text:
            sentiment = predict_sentiment(user_text)
            cleaned_preview = clean_text(user_text)
            summary, llm_status = ask_local_llm(user_text)
            if question:
                answer, answer_status = ask_local_llm(user_text, question)
                if answer_status != "Local LLM":
                    llm_status = answer_status

    return render_template(
        "index.html",
        user_text=user_text,
        question=question,
        sentiment=sentiment,
        summary=summary,
        answer=answer,
        llm_status=llm_status,
        cleaned_preview=cleaned_preview,
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)
