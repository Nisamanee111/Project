from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Page1"

@app.route('/second_url')
def add_second_page():
    return "Page2"

@app.route('/Third_url')
def add_Third_page():
    return "Page3"


if __name__ == "__main__" :
    app.run(debug=True)