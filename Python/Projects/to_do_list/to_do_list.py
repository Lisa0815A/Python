tasks = []

while True:
  print("\nTo-Do List:")
  print("1. Add a task")
  print("2. View tasks")
  print("3.Remove a tasks")
  print("4.exist")
  choice = input("Enter your choice (1-4) :")
  if choice == "1":
    task = input("Enter a new task:")
    tasks.append(task)
    print("Task added sucessfully!")
  elif choice == "2":
    if len(task) == 0:
      print("No task available.")
    else:
      print("\n your tasks:")
      for i,task in enumerate(tasks,1):
        print(i,".",task)
  elif choice == "3" :
    if len(tasks) == 0:
      task_num = int(input("Enter task number to remove:"))
      if 0<task_num <= len(tasks):
        removed_task = tasks.pop(task_num-1)
        print("Removed task:",removed_task)  
      else:
        print("Invalid task number")   
    elif choice == "4":
      print("Existing the TO-DO List App!")
      break
    else:
      print("Invalid choice.try again.") 
