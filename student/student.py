class Student:
  def __init__(self, name, age):
    self.name=name
    self.age=age
  def greet(self):
    print("Hi I'm "+ self.name)


stu_1=Student("Jhanvi",18)
stu_2=Student("Arshiya",17)

stu_1.greet()
stu_2.greet()

#change

print(stu_1.name)