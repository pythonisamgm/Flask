from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper_function():
       return f'<b>{function()}</b>'
    return wrapper_function()

def make_emphasis(function):
    pass
def make_underlined(function):
    pass

@app.route("/bye")
@make_bold
def bye():
    return "<p>Bye, World!</p>"

bye()
if __name__ == "__main__":
    app.run(debug=True)

