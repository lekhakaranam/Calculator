from flask import Flask, render_template
from expression_evaluator import ExpressionEvaluator
from Infix_Postfix import InfixToPostfix
import math
app = Flask(__name__)


@app.route('/balance')
def index():
    return render_template('index.html')


@app.route('/calculate', methods=['GET', 'POST'])
def calculate(number_string_to_parse):
    exp = ExpressionEvaluator()
    pass


@app.route('/squareroot', methods=['GET', 'POST'])
def squareroot(number):
    return math.sqrt(number)


@app.route('/cuberoot', methods=['GET', 'POST'])
def cuberoot(number):
    if number >= 0:
        return number ** (1. / 3.)
    return -(-number) ** (1. / 3.)


@app.route('/factorial', methods=['GET', 'POST'])
def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)


if __name__ == "__main__":
    app.run(debug=True)
#is
#==