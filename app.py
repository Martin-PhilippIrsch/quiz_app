from flask import Flask, render_template, request, jsonify
import json
import random
import os

app = Flask(__name__)

json_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'countries_and_capitals.json')
with open(json_file_path, "r") as file:
    data = json.load(file)

countries_and_capitals = {item["country"]: item["city"] for item in data}

def generate_question():
    country, capital = random.choice(list(countries_and_capitals.items()))
    options = [capital]
    while len(options) < 3:
        _, wrong_capital = random.choice(list(countries_and_capitals.items()))
        if wrong_capital not in options:
            options.append(wrong_capital)
    random.shuffle(options)
    return country, capital, options

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/next-question', methods=['POST'])
def next_question():
    country, correct_answer, options = generate_question()
    return jsonify({'country': country, 'correct_answer': correct_answer, 'options': options})

if __name__ == '__main__':
    app.run(debug=True)