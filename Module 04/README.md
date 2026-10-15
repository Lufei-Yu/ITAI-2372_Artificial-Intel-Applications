# AI in Finance - Build a simple Financial News Insight Application

A small educational prototype for analyzing finance-related text. It uses traditional NLP and machine learning to predict positive, negative, or neutral sentiment, and can use a locally running LLM to summarize an article or answer a question.

## Features

- Paste a financial headline or article into a simple web interface.
- Clean text using Python regular expressions.
- Convert text into TF-IDF features and classify sentiment with Naive Bayes.
- Generate a short summary and optional answer using a local LLM.
- Fall back to a simple extractive response if the LLM is unavailable.
- View the cleaned text used for sentiment analysis.

## Project files

- `app.py` — Flask web app and optional LLM connection.
- `model_training.py` — text cleaning, model training, and prediction.
- `sample_data.csv` — small example dataset with `text` and `label` columns.
- `templates/index.html` — web page.
- `static/style.css` — page styling.
- `requirements.txt` — Python dependencies.

## Requirements

- Python 3.10 or newer is recommended.
- Internet access is not required to run sentiment analysis after dependencies are installed.
- A local LLM is optional. The app works without one using a basic fallback summary.

## Install and run

1. Download or clone this project and open a terminal in the project folder.
2. Create and activate a virtual environment (recommended):

   **Windows**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

   **macOS/Linux**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Start the application:

   ```bash
   python app.py
   ```

   The app creates the model files automatically on first run. Open `http://127.0.0.1:5000` in a browser.

## Optional local LLM setup (Ollama)

1. Install Ollama and download a model supported by your computer, for example `llama3.2`.
2. Make sure Ollama is running.
3. Set the model name if needed:

   **Windows PowerShell**
   ```powershell
   $env:LLM_MODEL="llama3.2"
   $env:LLM_API_URL="http://localhost:11434/api/generate"
   python app.py
   ```

   **macOS/Linux**
   ```bash
   export LLM_MODEL="llama3.2"
   export LLM_API_URL="http://localhost:11434/api/generate"
   python app.py
   ```

If no local LLM is available, the app uses a simple text-based fallback. That fallback is not a true LLM response.

## How to test

1. Paste one of the following sample headlines into the app.
2. Click **Analyze text**.
3. Check the predicted sentiment and summary.
4. Enter a question such as “What risks does the article mention?” and analyze again.

**Positive example:** “Shares climbed after the company announced better-than-expected quarterly earnings.”

**Negative example:** “The company warned that falling demand may reduce revenue next quarter.”

**Neutral example:** “The company announced the date of its next quarterly report.”

## Method

1. **Preprocessing:** remove URLs and punctuation, normalize whitespace, and lowercase text.
2. **Feature extraction:** TF-IDF represents words and two-word phrases as numeric features.
3. **Sentiment classification:** a Multinomial Naive Bayes model predicts a sentiment label.
4. **LLM integration:** when configured, the app sends the article and task prompt to a local LLM endpoint.
5. **Interface:** Flask handles input and displays results in a browser.

## Business use case

A financial analyst or news aggregator could use this prototype to quickly screen a collection of financial headlines. Sentiment labels help identify items for closer review, while short summaries reduce the time needed to read each article. The prototype could be extended with a larger labeled dataset, source/date metadata, sector classification, and a dashboard of sentiment over time.

## Limitations and responsible use

- The included dataset is intentionally small and is only for demonstrating the workflow. Predictions may be wrong and are not representative of real-world model performance.
- The model is not specifically trained on a large professional financial sentiment corpus.
- A fallback summary is based on sentences from the supplied text and does not provide LLM-level reasoning.
- LLM outputs can omit context or produce incorrect information.
- The app does not predict stock prices and should not be used as the sole basis for an investment decision.
- This is an educational prototype, not financial advice.
