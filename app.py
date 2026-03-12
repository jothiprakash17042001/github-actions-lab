from flask import Flask
from calculator import add, subtract, multiply, divide

app = Flask(__name__)

@app.route("/")
def home():
    return "Calculator API Running"

@app.route("/add/<int:a>/<int:b>")
def add_numbers(a, b):
    return str(add(a, b))

@app.route("/sub/<int:a>/<int:b>")
def sub_numbers(a, b):
    return str(subtract(a, b))

@app.route("/mul/<int:a>/<int:b>")
def mul_numbers(a, b):
    return str(multiply(a, b))

@app.route("/div/<int:a>/<int:b>")
def div_numbers(a, b):
    try:
        return str(divide(a, b))
    except ValueError as e:
        return str(e), 400

if __name__ == "__main__":
    app.run()