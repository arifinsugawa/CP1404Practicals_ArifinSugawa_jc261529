from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1> Hello World! :) <h1>'

@app.route('/greet')
@app.route('/greet/<name>')
def greet(name = ""):
    return "Hello {}".format(name)

@app.route('/convert')
@app.route('/convert/<degree>')
def convert(degree = 0):
    try:
        CONST_FahrenheitConvert = 5/9
        fahrenheit = (int(degree) - 32) * CONST_FahrenheitConvert
        return "<h1> {} degree is {:.2f} fahrenheit <h1> ".format(degree, fahrenheit)

    except ValueError:
        return "Degree provided is not number" 


if __name__ == '__main__':
    app.run()


