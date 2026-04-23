from flask import Flask, request, jsonify
import task_manager as tm

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello!!! Welcome to Task Manager"

@app.route("/tasks", methods = ["GET"])
def get_tasks():
    return jsonify(tm.load_tasks())

@app.route("/tasks", methods = ["POST"])
def add_tasks():
    data = request.json
    tm.add_task(data["task"])
    return {"message": "Task added"}

@app.route("/tasks/<int:id>", methods = ["DELETE"])
def delete_task(id):
    tm.delete_task(id)
    return {"message": "Task deleted"}

@app.route("/tasks/<int:id>", methods = ["PUT"])
def mark_done(id):
    tm.mark_done(id)
    return {"message": "Task updated"}

if __name__=="__main__":
    app.run(app.run(host="0.0.0.0", port=5000))
