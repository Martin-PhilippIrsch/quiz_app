from flask import Flask, render_template, request, redirect, url_for, flash
import random
import json
#import secrets

#when deployed, provide full path
with open("countries_and_capitals.json", "r") as f:
    data = json.load(f)

countries_and_capitals = {item["country"]: item["city"] for item in data}

app = Flask(__name__)
app.secret_key = "639d7e02a4ec6653752f3f739604ad9c"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        answer = request.form['answer']
        correct_answer = request.form['correct_answer']
        country = request.form['country']
        if answer == correct_answer:
            flash("Correct!", "success")
        else:
            flash(f"Incorrect! The capital of {country} is {correct_answer}.", "danger")
        return redirect(url_for('index'))

    country, correct_answer, options = generate_question()
    return render_template('index.html', country=country, correct_answer=correct_answer, options=options)

def generate_question():
    country = random.choice(list(countries_and_capitals.keys()))
    correct_answer = countries_and_capitals[country]
    options = [correct_answer] + random.sample(list(countries_and_capitals.values()), 2)
    random.shuffle(options)
    return country, correct_answer, options

if __name__ == '__main__':
    app.run(debug=True)
