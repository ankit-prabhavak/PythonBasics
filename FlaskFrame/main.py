from flask import Flask, request, render_template

app = Flask(__name__)

tasks = []

@app.route('/')
def home():
    return render_template('index.html', tasks=tasks)

@app.route('/add-task', methods=['POST'])
def add_task():
    task = request.form.get('task')
    tasks.append(task)
    return render_template('index.html', tasks=tasks)

if __name__ == '__main__':
    app.run(debug=True)

