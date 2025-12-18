from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'


@app.route('/print/<string:text>')
def print_text(text):
    # print to console
    print(text)
    # return to browser
    return text


@app.route('/count/<int:num>')
def count(num):
    output = ''
    for i in range(num):
        output += f"{i}\n"
    return output


@app.route('/math/<int:a>/<op>/<int:b>')
def math(a, op, b):
    if op == '+':
        result = a + b
    elif op == '-':
        result = a - b
    elif op == '*':
        result = a * b
    elif op == 'div':
        result = a / b
    elif op == '%':
        result = a % b
    else:
        return 'Invalid operation', 400

    return str(result)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
