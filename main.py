from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/say/')
@app.route('/say/<something>')
def hello(something=None):
    return render_template('say.html', something=something)


if __name__ == "__main__":
    app.run()