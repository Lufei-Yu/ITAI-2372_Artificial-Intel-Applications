# AI Product Description Generator (Flask)

A classroom Flask app that generates retail product descriptions using Hugging Face Transformers.
Users enter a product name, comma-separated keywords, and a writing tone.

## Files
- `app.py` — Flask routes and LLM generation function
- `templates/index.html` — web form and output display
- `requirements.txt` — dependencies

## Run locally
1. Install Python 3.9 or newer.
2. (Optional) Create and activate a virtual environment.
3. Install dependencies:

   `pip install -r requirements.txt`

4. Start the app:

   `python app.py`

5. Open http://127.0.0.1:5000/ in your browser.

The first run downloads the GPT-2 model and may take several minutes. An internet connection is needed for the initial download.

## Notes
The default model is `gpt2`. You can set the `MODEL_NAME` environment variable to another compatible Hugging Face text-generation model. Review all generated product claims before publishing. This demo uses Flask debug mode for local testing only; disable it for deployment.
