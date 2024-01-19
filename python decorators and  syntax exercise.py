from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper():
       return '<b>' + function() +'</b>'
    return wrapper

def make_emphasis(function):
    def wrapper():
        return '<em>' + function() +'</em>'
    return wrapper
def make_underlined(function):
    def wrapper():
        return '<u>' + function() +'</u>'
    return wrapper

@app.route("/bye")
@make_bold
@make_underlined
@make_emphasis
def bye():
    return "<p>Bye, World!</p>"

if __name__ == "__main__":
    app.run(debug=True)

