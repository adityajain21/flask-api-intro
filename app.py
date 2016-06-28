#!flask/bin/python
from flask import Flask, jsonify,render_template, request

app = Flask(__name__)

tasks = [
    {
        'name': u'Aditya Jain',
        'phone_no': u'769',
    },
    {
        'name': u'Kanak Thakkar',
        'phone_no': u'765',
    }
]

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


@app.route('/tasks',methods=['POST'])
def create_task():
    task={
    'name':request.form['name'],
    'phone_no':request.form['ph_no']
    }

    tasks.append(task)
    return jsonify({'task': tasks}), 201

if __name__ == '__main__':
    app.run(debug=True)