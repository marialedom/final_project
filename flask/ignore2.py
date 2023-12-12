from flask import Flask, render_template, request

app = Flask(__name__)

tasks = []

@app.route('/')
def index():
    return render_template('finalproject.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    title = request.form.get('title')
    description = request.form.get('description')
    subject = request.form.get('subject')
    due_date = request.form.get('due-date')
    topics = request.form.get('topics').split(',') if request.form.get('topics') else []

    new_task = {
        'title': title,
        'description': description,
        'subject': subject,
        'start': due_date,
        'topics': topics
    }

    tasks.append(new_task)

    return render_template('finalproject.html', tasks=tasks)

if __name__ == '__main__':
    app.run(debug=True)
