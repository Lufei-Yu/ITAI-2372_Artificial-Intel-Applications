import os
import re
import logging

from flask import Flask, render_template, request
import torch
from transformers import pipeline

app = Flask(__name__)
MODEL_NAME = os.getenv("MODEL_NAME", "gpt2")
DEVICE = 0 if torch.cuda.is_available() else -1

try:
    generator = pipeline("text-generation", model=MODEL_NAME, device=DEVICE)
    MODEL_ERROR = None
except Exception as exc:
    generator = None
    MODEL_ERROR = str(exc)

ALLOWED_TONES = {
    "neutral", "formal", "casual", "humorous",
    "for young adults", "for professionals"
}

def generate_description(product_name, keywords, tone="neutral"):
    product_name = (product_name or "").strip()
    if not product_name:
        raise ValueError("Please enter a product name.")

    keyword_list = [x.strip() for x in (keywords or "").split(",") if x.strip()]
    if not keyword_list:
        raise ValueError("Please enter at least one keyword.")

    if tone not in ALLOWED_TONES:
        tone = "neutral"

    if generator is None:
        raise RuntimeError(
            "The model could not be loaded. Check your installation and internet "
            f"connection, then restart the app. Details: {MODEL_ERROR}"
        )

    prompt = (
        "Write one concise, compelling online retail product description. "
        f"Product: {product_name}. Keywords: {', '.join(keyword_list)}. "
        f"Tone: {tone}. Use the keywords naturally. Do not invent specifications, "
        "certifications, performance claims, or guarantees. Product description:"
    )

    output = generator(
        prompt,
        max_new_tokens=100,
        num_return_sequences=1,
        do_sample=True,
        temperature=0.8,
        top_p=0.9,
        repetition_penalty=1.15,
        pad_token_id=generator.tokenizer.eos_token_id,
    )[0]["generated_text"]

    description = output[len(prompt):].strip()
    description = re.split(r"\\n\\s*\\n", description)[0].strip()
    description = re.sub(r"\\s+", " ", description)
    if not description:
        raise RuntimeError("The model returned an empty description. Please try again.")
    return description


@app.route("/", methods=["GET", "POST"])
def index():
    description = None
    error = None
    product_name = ""
    keywords = ""
    tone = "neutral"

    if request.method == "POST":
        product_name = request.form.get("product_name", "")
        keywords = request.form.get("keywords", "")
        tone = request.form.get("tone", "neutral")
        try:
            description = generate_description(product_name, keywords, tone)
        except (ValueError, RuntimeError) as exc:
            error = str(exc)
        except Exception:
            app.logger.exception("Unexpected generation error")
            error = "Something went wrong. Please try again."

    return render_template(
        "index.html",
        description=description,
        error=error,
        product_name=product_name,
        keywords=keywords,
        tone=tone,
        model_name=MODEL_NAME,
    )


if __name__ == "__main__":
    # For local classroom testing only. Disable debug mode when deploying.
    app.run(host="127.0.0.1", port=5000, debug=True)
