# app_2.py

from flask import Flask, render_template, request, redirect, url_for, jsonify
import OOP_FUNCTIONS

app = Flask(__name__)
to_do_list = OOP_FUNCTIONS.ToDoList()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        subject = request.form['subject']
        due_date = request.form['due_date']
        topics = request.form['topics'].split(',') if request.form['topics'] else []
        status = request.form['status']

        new_task = OOP_FUNCTIONS.Task(title, description, subject, due_date, topics)
        to_do_list.add_task(new_task)
        return redirect(url_for('index'))

    return render_template('dashboard.html', tasks=to_do_list.get_all_tasks())

@app.route('/', methods=['GET', 'POST'])
def task_adding():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        subject = request.form['subject']
        due_date = request.form['due_date']
        topics = request.form['topics'].split(',') if request.form['topics'] else []

        new_task = OOP_FUNCTIONS.Task(title, description, subject, due_date, topics)
        to_do_list.add_task(new_task)
        return redirect(url_for('index'))

    return render_template('tasks_adding.html', tasks=to_do_list.get_all_tasks())

@app.route('/filter_tasks', methods=['POST'])
def filter_tasks():
    filter_type = request.form.get('filter_type')
    filter_value = request.form.get('filter_value')
    filtered_tasks = to_do_list.filter_tasks(filter_type, filter_value)
    # Convert filtered_tasks to a suitable format for returning to the frontend
    return jsonify(filtered_tasks)

if __name__ == '__main__':
    app.run(debug=True)
