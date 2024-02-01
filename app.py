from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Replace 'your_username', 'your_password', 'your_database_name' with your MySQL credentials
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://your_database_name:your_password@localhost/your_database_name'

db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200), nullable=False)
    reminder = db.Column(db.String(50))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/tasks', methods=['GET', 'POST'])
def tasks():
    if request.method == 'POST':
        data = request.json
        new_task = Task(text=data['text'], reminder=data['reminder'])
        db.session.add(new_task)
        db.session.commit()
        return jsonify({'message': 'Task added successfully!'})

    elif request.method == 'GET':
        tasks = Task.query.all()
        task_list = [{'id': task.id, 'text': task.text, 'reminder': task.reminder} for task in tasks]
        return jsonify({'tasks': task_list})

@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({'message': 'Task deleted successfully!'})

if __name__ == '__main__':
    # Create tables only if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)