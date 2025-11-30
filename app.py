from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "<h1>Hello World :)</h1>"


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"


def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return celsius * 9.0 / 5 + 32


@app.route('/convert/<celsius>')
def convert(celsius):
    """Convert Celsius value from URL and display Fahrenheit."""
    try:
        celsius_float = float(celsius)
        fahrenheit = celsius_to_fahrenheit(celsius_float)
        return f"<p>{celsius_float}°C is {fahrenheit:.2f}°F</p>"
    except ValueError:
        return "<p>Invalid number. Please enter a valid Celsius value.</p>"


if __name__ == '__main__':
    app.run(debug=True)
