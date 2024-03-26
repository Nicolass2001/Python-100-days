from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def inner_function():
        return f"<b>{function()}</b>"
    return inner_function

def make_emphasis(function):
    def inner_function():
        return f"<em>{function()}</em>"
    return inner_function

def make_underlined(function):
    def inner_function():
        return f"<u>{function()}</u>"
    return inner_function

@app.route("/")
@make_bold
@make_emphasis
@make_underlined
def hello_world():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True)