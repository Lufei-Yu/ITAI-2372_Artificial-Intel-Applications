# Templates Folder

This folder contains the HTML files used by the Flask application.

## index.html

The `index.html` file is the main webpage for the AI Product Description Generator. It provides a simple interface where users can enter product information and generate descriptions using AI.

### Main Features

- **Product Name:** Allows users to enter a product name.
- **Keywords:** Allows users to enter keywords separated by commas.
- **Writing Tone:** Provides different tone options, such as neutral, formal, casual, and humorous.
- **Generate Button:** Sends the information to the Flask application.
- **Output Section:** Displays the AI-generated product description or error messages.

### How It Works

1. The user opens the webpage in a browser.
2. The user enters a product name and keywords.
3. The user selects a writing tone.
4. The form sends the information to the Flask application.
5. The AI model generates a product description.
6. The generated description is displayed on the webpage.

### Flask Integration

The HTML template uses Jinja syntax to communicate with Flask. It receives information from `app.py` and displays the generated description using template variables.


