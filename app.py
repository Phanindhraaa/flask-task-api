from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = []

@app.route("/")
def hello_world():
    return "<p>HELLO, DRUHIIII!</p>"

@app.route("/health")
def health_check():
    return jsonify({"status": "healthy"})

@app.route("/tasks")
def get_tasks():
    return jsonify({"tasks": tasks})

@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()
    task = data.get("task")
    tasks.append(task)
    return jsonify({"message": "Task added", "task": task})
