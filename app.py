from flask import Flask, render_template, request, redirect, url_for
import csv
import random
from datetime import datetime

app = Flask(__name__)

# List of random quotes
quotes = [
    "The best way to predict the future is to invent it.",
    "Life is 10% what happens to us and 90% how we react to it.",
    "Your time is limited, so don't waste it living someone else's life.",
    "The only limit to our realization of tomorrow is our doubts of today."
]

# Path to the CSV file
CSV_FILE = 'submissions.csv'

# Route for the home page (GET request)
@app.route('/')
def home():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    random_quote = random.choice(quotes)
    return render_template('index.html', current_time=current_time, random_quote=random_quote)

# Route to handle form submission (POST request)
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']

    # Write the form data to the CSV file
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, email])

    return redirect(url_for('submissions'))

# Route to display the stored data
@app.route('/submissions')
def submissions():
    # Read the stored data from the CSV file
    submissions = []
    try:
        with open(CSV_FILE, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                submissions.append({'name': row[0], 'email': row[1]})
    except FileNotFoundError:
        submissions = []

    return render_template('submissions.html', submissions=submissions)

if __name__ == '__main__':
    app.run(debug=True)
