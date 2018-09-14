from flask import Flask, render_template, request
from base import engine, Base

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/say/')
@app.route('/say/<something>/')
def hello(something=None):
    return render_template('say.html', something=something)


@app.route("/task_completed/")
def task():
    return render_template('task.html')


@app.route('/task_completed/', methods=['POST'])
def task_post():
    name_task = request.form['name_task']
    task_description = request.form['task_description']
    responsible_for_the_task = request.form['responsible_for_the_task']
    task_end_date = request.form['task_end_date']
    return render_template('task_completed.html',
                           name_task=name_task,
                           task_description=task_description,
                           responsible_for_the_task=responsible_for_the_task,
                           task_end_date=task_end_date)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
