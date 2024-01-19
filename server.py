from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def home_page():
    return '<h1>Guess a number between 0 and 9</h1> ' \
           '<iframe src="https://giphy.com/embed/6OyrnAKxd46Rfall6K" width="480" height="480" frameBorder="0" ' \
           'class="giphy-embed" allowFullScreen></iframe>'

number = random.randint(0,9)
@app.route('/<int:user_number>')
def check_number(user_number):
    # show the post with the given id, the id is an integer

    if user_number > number:
        return "<h1 style='color:red'>Too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    elif user_number < number:
        return "<h1 style='color:green'>Too low, try again!</h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    elif user_number == number:
        return "<h1 style='color:blue'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"





if __name__ == "__main__":
    app.run(debug=True)

check_number()
