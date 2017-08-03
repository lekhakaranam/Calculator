from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calculate', methods=['GET', 'POST'])
def calculate(num1, num2, operator):
    pass


@app.route('/squareroot', methods=['GET', 'POST'])
def squareroot(number):
    pass


@app.route('/cuberoot', methods=['GET', 'POST'])
def cuberoot(number):
    pass


@app.route('/factorial', methods=['GET', 'POST'])
def calculate(number):
    pass


if __name__ == "__main__":
    app.run(debug=True)