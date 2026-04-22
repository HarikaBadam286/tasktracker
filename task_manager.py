import json

FILE = "tasks.json"

def load_tasks():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []
    
def save_tasks(tasks):
    with open(FILE, "w") as f:
        return json.dump(tasks, f)

def add_task(new_task):
    tasks = load_tasks()
    new_task_obj = {"id": len(tasks) + 1, "task": new_task, "status": "pending"}
    tasks.append(new_task_obj)
    save_tasks(tasks)
    print("Hurray!!! Task Added")

def list_tasks():
    tasks = load_tasks()
    for i in tasks:
        print(f"{i['id']}:  {i['task']}:  {i['status']}")

def mark_done(task_id):
    try:
        tasks = load_tasks()
        for t in tasks:
            if t["id"] == int(task_id):
                t["status"] = "done"
                break
        save_tasks(tasks)
        print("Yayyy!! You completed the task")
    except:
        print("enter a valid index")

def delete_task(task_id):
    tasks = load_tasks()
    tasks_new = []
    try:
        for t in tasks:
            if t["id"] != int(task_id):
                tasks_new.append(t)
        save_tasks(tasks_new)
        print("Task deleted;)")
    except:
        print("Please enter a valid index")

def display_help():
    print("""
          Hello!!! Welcome to Task Manager
          
          here you can do the following --->

          help ---- print this description
          add "<task>" ---- add a task to your task manager
          list ---- list all the tasks present in the task manager
          delete <index_of_task> ---- delete the task corresponding to the index given
    """
    )
