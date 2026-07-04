import json

def view_tasks(tasks):
  for index in tasks:
    print(index)

def add_tasks(tasks):
  add_tasks=input("Enter a task:")
  tasks.append(add_tasks)

def delete_task(tasks):
  delete_tasks=input("Enter task to be deleted:")
  tasks.remove(delete_tasks)

def save_tasks(tasks):
  with open("tasks.json","w") as f:
    json.dump(tasks,f)

def load_tasks():
  with open("tasks.json", "r")as f:
    data=json.load(f)
    return(data)
  
try:
    tasks = load_tasks()

except:
  tasks=[]


while True:
  
  options=input("what do you want to do add/view/delete")
  
  if options=="add":
    add_tasks(tasks)
    save_tasks(tasks)

  elif options=="view":
    view_tasks(tasks)
  
  elif options=="delete":
    delete_task(tasks)
    save_tasks(tasks)
