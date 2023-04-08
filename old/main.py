import tkinter as tk
import random
import json

# Load countries and capitals from the JSON file
with open("countries_and_capitals.json", "r") as f:
    data = json.load(f)

countries_and_capitals = {item["country"]: item["city"] for item in data}

def generate_question():
    country = random.choice(list(countries_and_capitals.keys()))
    correct_answer = countries_and_capitals[country]
    options = [correct_answer] + random.sample(list(countries_and_capitals.values()), 2)
    random.shuffle(options)
    return country, correct_answer, options

def check_answer():
    global score
    selected_option = options_var.get()
    if selected_option == correct_answer:
        result_var.set("Correct!")
        score += 1
    else:
        result_var.set(f"Incorrect! The capital of {country} is {correct_answer}.")
        score -= 1
    score_var.set(f"Score: {score}")

def next_question():
    global country, correct_answer, options
    country, correct_answer, options = generate_question()
    question_label.config(text=f"What is the capital of {country}?")
    for i, option in enumerate(options):
        radio_buttons[i].config(text=option, value=option)

    options_var.set(None)
    result_var.set("")

app = tk.Tk()
app.title("Capital City Quiz")

# Set fixed size for the app
app.minsize(450, 400)
app.maxsize(450, 400)

question_label = tk.Label(app, wraplength=300)
question_label.pack(pady=10)

options_var = tk.StringVar()

# Create a frame to hold the radio buttons
radio_frame = tk.Frame(app)
radio_frame.pack(anchor='center')

radio_buttons = []
for i in range(3):
    radio_button = tk.Radiobutton(radio_frame, variable=options_var, command=check_answer)
    radio_buttons.append(radio_button)
    radio_button.pack(anchor='w')

result_var = tk.StringVar()
result_label = tk.Label(app, textvariable=result_var)
result_label.pack(pady=10)

score = 0
score_var = tk.StringVar()
score_var.set(f"Score: {score}")
score_label = tk.Label(app, textvariable=score_var)
score_label.pack(pady=10)

next_button = tk.Button(app, text="Next Question", command=next_question)
next_button.pack(pady=10)

next_question()

app.mainloop()