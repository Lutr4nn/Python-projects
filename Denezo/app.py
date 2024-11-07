from flask import Flask, render_template, request, redirect, url_for
from database import Database

app = Flask(__name__)

db = Database(
    host="127.0.0.1",
    user="root",
    password="",
    database="denezo",
)

@app.route('/')
def index():
    tasks = db.query("SELECT * FROM tasks")
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    title = request.form.get('title')
    description = request.form.get('description')
    if title:
        db.execute("INSERT INTO tasks (title, description) VALUES (%s, %s)", (title, description))
    return redirect(url_for('index'))

@app.route('/delete_task/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    db.execute('DELETE FROM tasks WHERE id = %s', (task_id,))
    return redirect(url_for('index'))

@app.route('/update_task/<int:task_id>', methods=['POST'])
def update_task(task_id):
    title = request.form.get('title')
    description = request.form.get('description')
    if title and description:
        db.execute('UPDATE tasks SET title = %s, description = %s WHERE id = %s', (title, description, task_id))
    return redirect(url_for('index'))
    
 
if __name__ == '__main__':
    app.run(debug=True)
