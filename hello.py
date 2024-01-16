# save this as app.py
from flask import Flask

app = Flask(__name__)
print (__name__)


#------------------------------------------------ROUTE AND RENDERING HTML---------------------------
@app.route("/")
def hello_world():
    #rendering html. Be careful with single and double quotes
    return "<h1 style='text-align: center'>Hello, World!</h1>" \
           "<p>This is a paragraph</p>" \
           '<iframe src="https://giphy.com/embed/auxDaJxhVa2By" ' \
           'width="480" height="374" frameBorder="0" ' \
           'class="giphy-embed" allowFullScreen></iframe>'

@app.route("/bye")

def bye():
    return "<p>Bye, World!</p>"



#-------------------------------------------------ADD VARIABLES TO PARSING-----------------
#parsing URL: getting hold of what user typed after the "/" sign.
#add variable sections to a URL by marking sections with <variable name>. That name is going to render dinamically. @app.route("/var name")
@app.route("/username/<name>")
def greet(name):
    return f"Hello, {name}"

#------------------------------------------------RUN FLASK AND DEBUG MODE---------------------------
#debug mode: 1)activates the debugger; 2)activates the automatic reloader; 3) enables the debug mode on the flask app.

if __name__ == "__main__":
    app.run(debug=True)

#----------------------------------------------------CONVERTER--------------------------------------
#converts the URL into any data type that you specify by default (by default, a string)
#@app.route("/username/<name>/int:number")
#def greet(name):
#    return f"Hello, {name}, you are {number} years old!"

#---------------------
