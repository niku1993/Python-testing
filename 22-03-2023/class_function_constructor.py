"""
class Employee :
    no_of_leaves = 8
    def __init__(self, aname, asalary, arole):
        self.name=aname
        self.salary=asalary
        self.role=arole
    def printdetials (self):
        return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"

Harry = Employee ('Harry', 255, 'Instructor')

print (Harry.printdetials())
"""

#create a Class For 5 Students, their name and marks in English, Maths, Physics, Chemistry, Computer Science

class Students :
    def __init__(self, name, marks_1, marks_2, marks_3, marks_4, marks_5):
        self.student_name = name
        self.english = marks_1
        self.maths = marks_2
        self.physics = marks_3
        self.chemistry = marks_4
        self.computer_science = marks_5

    def printscore_card (self):
        return f"Name is {self.student_name}. Marks in English {self.english}, Marks in Maths {self.maths}, Marks in Physics {self.physics}, Marks in Chemistry {self.chemistry}, Marks in Computer Science {self.computer_science}"

    def __add__(self):
        sum=self.english+self.maths+self.physics+self.chemistry+self.computer_science;
        return f"Total marks of {self.student_name} is {sum}"

    def percentage (self):
      sum2 = self.english + self.maths + self.physics + self.chemistry + self.computer_science
      return f"Percentage of {self.student_name} is  {sum2*100 / 500}"

Nitish = Students ("Nitish", 82, 86, 89, 87, 77)
Priya = Students ("Priya", 96, 97, 79, 89, 75)
Tanya = Students ("Tanya", 88, 81, 91, 83, 88)
Himanshu = Students ("Himanshu", 87, 82, 88, 90, 95)
Gunnu = Students ("Garamjeet", 00, 00, 00, 00, 00)

print(Nitish.printscore_card())
print(Priya.printscore_card())
print (Tanya.printscore_card())
print (Himanshu.printscore_card())
print (Gunnu.printscore_card())

print(Nitish.__add__())
print(Priya.__add__())
print(Tanya.__add__())
print(Himanshu.__add__())
print(Gunnu.__add__())

print(Nitish.percentage())
print(Priya.percentage())
print(Tanya.percentage())
print(Himanshu.percentage())
print(Gunnu.percentage())