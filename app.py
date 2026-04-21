import sys
import task_manager as tm

cmd = sys.argv[1]

if cmd == "add":
    tm.add_task(sys.argv[2])
elif cmd == "list":
    tm.list_tasks()
elif cmd == "delete":
    tm.delete_task(sys.argv[2])
elif cmd == "help":
    tm.display_help()
else:
    print("Please enter valid option")
    tm.display_help()