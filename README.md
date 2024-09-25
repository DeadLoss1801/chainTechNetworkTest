# Flask Dynamic Web Page with Form Submission

This project is a simple Flask-based web server that serves a dynamic HTML page with user input forms. The project allows users to submit their details (name, email), stores the submissions in a CSV file, and displays the submitted data on a separate page.

## Features
- Displays dynamic content such as the current date/time and random quotes.
- Allows users to submit their name and email via a form.
- Stores form submissions in a CSV file.
- Displays stored submissions on a separate page.
- Includes styled HTML templates using CSS.
- Redirects users to the submissions page after form submission.

## Technologies Used
- **Python**: For the backend server.
- **Flask**: A lightweight web framework for Python.
- **HTML/CSS**: For the frontend UI.
- **CSV**: Used for storing form submissions.

## Setup and Installation

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/flask-form-submission.git
cd flask-form-submission
```


### 2. Set up a virtual environment (Optional but recommended)
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Run the Flask app
```bash
pip install Flask
python app.py
```