# AI Product Description Generator (Flask)

A classroom Flask app that generates retail product descriptions using Hugging Face Transformers.
Users enter a product name, comma-separated keywords, and a writing tone.

---

## Features

- **Dynamic Generation:** Leverages pre-trained Hugging Face transformer models (GPT-2) to produce creative and contextual product text.
- **Customizable Inputs:** Input specific product names, custom keywords, and tones to tailor the output description.
- **Web Interface:** Includes an interactive HTML frontend form for easy user interaction and instant results display.
- **Dual Formats:** Available as both a standard Flask application (`app.py`) and a Jupyter Notebook version (`AI_Product_Description.ipynb`) for interactive development and testing.

---

## Files
- `app.py` — Flask routes and LLM generation function
- `templates/index.html` — web form and output display
- `requirements.txt` — dependencies


## Installation & Setup
1. Clone or download the repository to your local machine.
2. Navigate into the Module 06 directory.
3. (Optional) Create and activate a virtual environment:

  python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate


4. Install dependencies:

pip install -r requirements.txt

## Running the Application

1. Start the Flask server:

python app.py

2. Open your browser and navigate to:http://127.0.0.1:5000/

The first run downloads the GPT-2 model and may take several minutes. An internet connection is needed for the initial download.

## Usage
1. Enter the target Product Name into the web form.

2. Provide a list of Keywords separated by commas (e.g., lightweight, waterproof, durable).

3. Select or enter your desired Writing Tone (e.g., professional, enthusiastic, casual).

4. Click Generate to view the AI-crafted product description.

