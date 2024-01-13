# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult ,div

app = Flask(__name__)

@app.route("/add")
def do_add():
    """Add a and b parameters."""

    a = int(request.args.get("a", 0))
    b = int(request.args.get("b", 0))
    result = add(a, b)

    return str(result)

@app.route("/sub")
def do_sub():
    """Substract a and b parameters"""

    a = int(request.args.get("a", 0))
    b = int(request.args.get("b", 0))
    result = sub(a, b)

    return str(result)

@app.route("/mult")
def do_mult():
    """Multiply a and b parameters"""
    a = int(request.args.get("a", 0))
    b = int(request.args.get("b", 0))
    result = mult(a, b)

    return str(result)

@app.route("/div")
def do_div():
    """Divide a and b parameters"""
    a = int(request.args.get("a", 0))
    b = int(request.args.get("b", 0))
    result = div(a, b)

    return str(result)


# Using Variables

operators = {
        "add": add,
        "sub": sub,
        "mult": mult,
        "div": div,
        }

@app.route("/math/<oper>")
def do_math(oper):
    """Do math on a and b"""
    
    a = int(request.args.get("a", 0))
    b = int(request.args.get("b", 0))

    result = operators[oper](a, b)

    return str(result)