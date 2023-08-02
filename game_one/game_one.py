from flask import Flask, render_template, request
import random
import os

app = Flask(__name__)

current_folder = os.path.dirname(os.path.abspath(__file__))
files_folder = os.path.dirname(current_folder)
txt_file = os.path.join(files_folder, "words.txt")

with open(txt_file, 'r') as file:
    words = [word.strip() for word in file.readlines()]

words = [word.lower() for word in words]

matching_word = random.choice(words)
table_up = []
table_down = []
matched_letters = ["_","_","_","_","_"]


def how_many(word_user):
    for i in range(len(matching_word)):
        if matching_word[i] == word_user[i]:
            matched_letters[i] = word_user[i]
        else:
            break

@app.route('/')
def index():
    return render_template('game_one_index.html', table_up=table_up, table_down=table_down)


@app.route('/', methods=['POST'])
def play_game():
    print(matching_word)
    word_user = request.form['word']
    word_user.lower()
    readonly = ""

    if len(word_user) < 5:
        word = 'Word must have at least 5 letters'
        color = "red"

    else:
        if word_user in words:
            how_many(word_user)
            if word_user == matching_word:
                word = 'Correct: ' + word_user
                color = "green"
                readonly = "readonly"
            else:
                word = 'Wrong word'
                color = "red"

                if word_user > matching_word:
                    table_down.append(word_user)
                    table_down.sort()
                if word_user < matching_word:
                    table_up.append(word_user)
                    table_up.sort()
        else:
            word = "This word does not exist"
            color = "red"

    password = ' '.join(str(element) for element in matched_letters)

    return render_template('game_one_index.html', word=word, table_up=table_up, table_down=table_down,
                           color=color, letters=password, readonly=readonly)


if __name__ == '__main__':
    app.run()