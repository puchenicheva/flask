from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
# def index():
#     return render_template('index.html')
#
#
# @app.route('/say/')
# @app.route('/say/<something>/')
# def hello(something=None):
#     return render_template('say.html', something=something)


@app.route("/task/")
def task():
    return render_template('task.html')


@app.route('/task/', methods=['POST'])
def task_post():
    # name_task = request.form['name_task']
    # task_description = request.form['task_description']
    # responsible_for_the_task = request.form['responsible_for_the_task']
    # task_end_date = request.form['task_end_date']
    return render_template('task_completed.html',
                           name_task=request.form['name_task'],
                           task_description=request.form['task_description'],
                           responsible_for_the_task=request.form['responsible_for_the_task'],
                           task_end_date=request.form['task_end_date'])


if __name__ == "__main__":
    app.run()