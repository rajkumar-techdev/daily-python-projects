#To-Do List(Console Application)
from operator import index


def todo_list():
    tasks=[]
    while True:
        print("\n To-Do List Menu")
        print("1.Add Task")
        print("2.View Task")
        print("3.Delete Task")
        print("4.Update Task")
        print("5.Exit")

        choice=input("Enter your choice")
        #Add Task
        if choice=='1':
            task=input("Enter task: ")
            tasks.append(task)
            print("Task added")
        #View Task
        elif choice=='2':
            print("\n Your Tasks")
            for idx,task in enumerate(tasks,start=1):
                print(f"{idx},{task}")
        #Delete Task
        elif choice=='3':
            try:
                index1=int(input("Enter task number to delete"))
                removed=tasks.pop(index1-1)
                print(f"Removed: {removed}")
            except (IndexError,ValueError):
                print("Invalid Task Number")
        elif choice=='4':
            idx=int(input("Enter index number: "))
            task =input("Enter Task name to Update:")
            tasks[idx]=task
            print("Task Updated")
        elif choice=='5':
            print("Good Bye")
            break
        else:
            print("Invalid Choice,Try Again")

todo_list()
