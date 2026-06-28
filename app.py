"""Name=input("enter a name")
Object=input("enter an object")
Place=input("enter a Place")
Creature=input("enter a Creature")
Planet=input("enter a Planet")
Vehicle=input("enter a Vehicle")
Treasure=input("enter a Treasure")
Character=input("enter a Character")
Weather_condition=input("enter a Weather condition")
Skill=input("enter a Skill")
Plural_animal=input("enter a Plural animal")
Tool=input("enter a Tool")
Adjective=input("enter a Adjective")
Noun=input("enter a Noun")
Verb=input("enter a Verb")
Festival=input("enter a Festival")
Food=input("enter a Food")
Drink=input("enter a Drink")
Job=input("enter a Job")

print("The Secret Robot Adventure- One day,"+Name+"found a mysterious"+Object+"lying near a"+Place+". When they touched it, a tiny"+Creature+"appeared and said You have been chosen for a special mission!"
      "The mission was to travel to a"+Planet+"using a"+Vehicle+"and recover the lost"+Treasure+"from an evil"+Character+"."
      "On the journey,"+Name+"faced a"+Weather_condition+"and had to use their"+Skill+"to escape. Suddenly, a group of"+Plural_animal+"appeared and offered help with their magical"+Tool+
      "After reaching the destination, they discovered the treasure was actually a"+Adjective+Noun+"that could"+Verb+"the entire world."
      "Everyone celebrated by having a"+Festival+"with lots of"+Food+"and"+Drink+". From that day onwards,"+Name+"became known as the greatest"+Job+"in the universe.")

num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
op=input("Enter operation")

if op=="+":
  print(num1+num2)

elif op=="-":
  print(num1-num2)

elif op=="*":
  print(num1*num2)

elif op=="/":
  print(num1/num2)

else:
  print("Invalid")
  


month={
  "jan":"feb"
}

print(month.get("hi","invalid"))

word="jhanvi"
guess=""
guess_count=0
guess_limit=3
out_of_guess=False

while word!=guess and not out_of_guess:
  if guess_count<guess_limit:
     guess=input("enter your guess ")
     guess_count+=1
  else:
     out_of_guess=True

if out_of_guess:
    print("you are out of guesses")

else:
    print("you win")

   

def raise_to_power(base_num,power_num):
  result=1
  for index in range(power_num):
    result=result*base_num
  return result
  
print(raise_to_power(2,3))

def translate(phrase):
  translation=""
  for letter in phrase:
    if letter in "AEIOUaeiou":
      translation=translation+"g"
    else:
      translation=translation+letter
  return translation

print(translate(input("Enter a phrase:")))
"""

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
