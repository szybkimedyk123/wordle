from flask import Flask, render_template, request
import random
import os

app = Flask(__name__)
app.secret_key = 'secret_key'

current_folder = os.path.dirname(os.path.abspath(__file__))
files_folder = os.path.dirname(current_folder)
txt_file = os.path.join(files_folder, "words.txt")

with open(txt_file, 'r') as file:
    words = [word.strip() for word in file.readlines()]

words = [word.lower() for word in words]

matching_word = random.choice(words)

print(matching_word)
w1v = w2v = w3v = w4v = w5v = w6v = w7v = "hidden"
counter = 0
status = ""
word_1 = {
    "L1": {"letter": "_", "color": "grey"},
    "L2": {"letter": "_", "color": "grey"},
    "L3": {"letter": "_", "color": "grey"},
    "L4": {"letter": "_", "color": "grey"},
    "L5": {"letter": "_", "color": "grey"}
}
word_2 = {
    "L1": {"letter": "_", "color": "grey"},
    "L2": {"letter": "_", "color": "grey"},
    "L3": {"letter": "_", "color": "grey"},
    "L4": {"letter": "_", "color": "grey"},
    "L5": {"letter": "_", "color": "grey"}
}
word_3 = {
    "L1": {"letter": "_", "color": "grey"},
    "L2": {"letter": "_", "color": "grey"},
    "L3": {"letter": "_", "color": "grey"},
    "L4": {"letter": "_", "color": "grey"},
    "L5": {"letter": "_", "color": "grey"}
}
word_4 = {
    "L1": {"letter": "_", "color": "grey"},
    "L2": {"letter": "_", "color": "grey"},
    "L3": {"letter": "_", "color": "grey"},
    "L4": {"letter": "_", "color": "grey"},
    "L5": {"letter": "_", "color": "grey"}
}
word_5 = {
    "L1": {"letter": "_", "color": "grey"},
    "L2": {"letter": "_", "color": "grey"},
    "L3": {"letter": "_", "color": "grey"},
    "L4": {"letter": "_", "color": "grey"},
    "L5": {"letter": "_", "color": "grey"}
}
word_6 = {
    "L1": {"letter": "_", "color": "grey"},
    "L2": {"letter": "_", "color": "grey"},
    "L3": {"letter": "_", "color": "grey"},
    "L4": {"letter": "_", "color": "grey"},
    "L5": {"letter": "_", "color": "grey"}
}
alphabet = {
    "A": "black",
    "B": "black",
    "C": "black",
    "D": "black",
    "E": "black",
    "F": "black",
    "G": "black",
    "H": "black",
    "I": "black",
    "J": "black",
    "K": "black",
    "L": "black",
    "M": "black",
    "N": "black",
    "O": "black",
    "P": "black",
    "Q": "black",
    "R": "black",
    "S": "black",
    "T": "black",
    "U": "black",
    "V": "black",
    "W": "black",
    "X": "black",
    "Y": "black",
    "Z": "black"
}

@app.route('/')
def index():
    return render_template('index.html', alphabet=alphabet, hidden1=w1v, hidden2=w2v, hidden3=w3v,
                           hidden4=w4v, hidden5=w5v, hidden6=w6v, hidden7=w7v, word_1=word_1, word_2=word_2,
                           word_3=word_3, word_4=word_4, word_5=word_5, word_6=word_6)

if __name__ == '__main__':
    app.run()