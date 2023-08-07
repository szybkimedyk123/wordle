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


def alphabet_change(word_user, alphabet_dic, matching):
    for letter in word_user:
        if letter in matching:
            letter = letter.upper()
            alphabet_dic[letter] = "green"
        else:
            letter = letter.upper()
            alphabet_dic[letter] = "white"

    return alphabet_dic


def word_check(word, word_user, matching):
    i = 0
    found_letters = set()
    found_positions = set()
    matching_counts = {letter.upper(): matching.count(letter.upper()) for letter in set(matching)}

    for letter in word_user:
        l1 = letter.upper()
        word[f"L{i + 1}"]["letter"] = l1

        if l1 == matching[i].upper():
            word[f"L{i + 1}"]["color"] = "DarkGreen"
            found_letters.add(l1)
            found_positions.add(i)
        elif l1 in matching_counts and l1 not in found_letters:
            matching_count = matching_counts[l1]
            user_count = word_user.upper().count(l1)
            if i in found_positions or user_count >= matching_count:
                word[f"L{i + 1}"]["color"] = "orange"
            else:
                word[f"L{i + 1}"]["color"] = "DarkGreen"
            found_letters.add(l1)
        else:
            word[f"L{i + 1}"]["color"] = "black"

        i += 1

    return word

@app.route('/')
def index():
    return render_template('index.html', alphabet=alphabet, hidden1=w1v, hidden2=w2v, hidden3=w3v,
                           hidden4=w4v, hidden5=w5v, hidden6=w6v, hidden7=w7v, word_1=word_1, word_2=word_2,
                           word_3=word_3, word_4=word_4, word_5=word_5, word_6=word_6)


@app.route('/', methods=['GET', 'POST'])
def word_game():
    global counter, w1v, w2v, w3v, w4v, w5v, w6v, w7v, word_1, word_2, word_3, word_4, word_5, word_6, status

    word_user = request.form['word']
    word_user.lower()

    if word_user in words:
        alphabet_color = alphabet_change(word_user, alphabet, matching_word)

        counter += 1

        if counter == 1:
            word_1 = word_check(word_1, word_user, matching_word)
            w1v = "visible"
        elif counter == 2:
            word_2 = word_check(word_2, word_user, matching_word)
            w2v = "visible"
        elif counter == 3:
            word_3 = word_check(word_3, word_user, matching_word)
            w3v = "visible"
        elif counter == 4:
            word_4 = word_check(word_4, word_user, matching_word)
            w4v = "visible"
        elif counter == 5:
            word_5 = word_check(word_5, word_user, matching_word)
            w5v = "visible"
        elif counter == 6:
            word_6 = word_check(word_6, word_user, matching_word)
            w6v = "visible"

        if word_user == matching_word or counter == 6:
            readonly = "readonly"
            if counter < 6:
                status = "You won."
            else:
                status = "You lost. Answer is " + matching_word.upper()
            w7v = "visible"
        else:
            readonly = ""
            w7v = "hidden"

    else:
        readonly = ""
        alphabet_color = alphabet
        w7v = "visible"
        status = "This word does not exist"

    return render_template('index.html', alphabet=alphabet_color, word_1=word_1, word_2=word_2,
                           word_3=word_3, word_4=word_4, word_5=word_5, word_6=word_6, hidden1=w1v, hidden2=w2v,
                           hidden3=w3v, hidden4=w4v, hidden5=w5v, hidden6=w6v, hidden7=w7v, readonly=readonly, status=status)

if __name__ == '__main__':
    app.run()