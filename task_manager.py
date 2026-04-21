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
    tasks.append(new_task)
    save_tasks(tasks)
    print("Hurray!!! Task Added")

def list_tasks():
    tasks = load_tasks()
    for i, t in enumerate(tasks):
        print(f"{i}:  {t}")

def delete_task(index):
    tasks = load_tasks()
    try:
        tasks.pop(int(index))
        save_tasks(tasks)
        print("yayyy!! Task deleted i.e., Task completed ;)")
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
