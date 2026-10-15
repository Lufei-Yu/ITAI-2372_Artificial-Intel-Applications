# Static Folder

## Overview
The `static` folder contains the files used to control the appearance and styling of the Finance Insights App.

## Files

### `style.css`
This file contains the CSS styles for the application's web interface. It controls:

- Font styles, text sizes, and colors.
- Page layout and spacing.
- Input fields and buttons.
- Result cards displaying sentiment analysis and summaries.
- Sentiment labels for positive, negative, and neutral results.
- Responsive layout for different screen sizes.

## How It Works
The `index.html` file in the `templates` folder links to `style.css` using Flask's `url_for()` function. When users open the application, the browser loads the CSS file to display the page with the correct styling.

## Purpose
The static folder keeps the styling separate from the HTML and Python code. This makes the application easier to organize, maintain, and customize.

