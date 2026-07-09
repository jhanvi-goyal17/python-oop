class Student:
  school="ABC School"

  num_of_students=0
  
  def __init__(self, name, age):
    self.name=name
    self.age=age
    Student.num_of_students += 1
  def greet(self):
    print("Hi I'm "+ self.name +" and I'm "+ str(self.age) +" years old, From " + Student.school)
  


stu_1=Student("Jhanvi",18)
stu_2=Student("Arshiya",17)

stu_1.greet()
stu_2.greet()  

print("Total number of students: ", Student.num_of_students)
