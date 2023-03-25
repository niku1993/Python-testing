# class trial:
#     def func(self):
#         a = 2
#         print(a)
#
#     def func1(self):
#         b = a
#         print(b)
#
# obj1=trial()
# obj2=trial()
#
# print(obj1.func())
# print(obj2.func1())

# WAP to add numbers from 1 to input number

# a= int(input("Enter end value : "))
# b=1
# sum=1
# while b<a:
#     b=b+1
#     sum=b+sum
#
# print (sum)

#Class method
#
# class Number:
#     pass
#
#     def __int__(self,number):
#         self.anumber = number
#
#     def func (self):
#         b=1
#         sum=1
#         while b<a:
#             b=b+1
#             sum=b+sum
#         print (sum)
#
#
# a = int(input("Enter end value : "))
# calculate = Number ()
#
# calculate.func()

# class Students :
#     num = 100
#
#     def __init__(self, name, marks_1, marks_2, marks_3, marks_4, marks_5):
#         self.student_name = name
#         self.english = marks_1
#         self.maths = marks_2
#         self.physics = marks_3
#         self.chemistry = marks_4
#         self.computer_science = marks_5
#
#     def printscore_card (self):
#         return f"Name is {self.student_name}. Marks in English {self.english}, Marks in Maths {self.maths}, Marks in Physics {self.physics}, Marks in Chemistry {self.chemistry}, Marks in Computer Science {self.computer_science}"
#
#     def prap(self):
#
#
#     def __add__(self):
#         sum=self.english+self.maths+self.physics+self.chemistry+self.computer_science;
#         return f"Total marks of {self.student_name} is {sum}"
#
#     def percentage (self):
#       sum2 = self.english + self.maths + self.physics + self.chemistry + self.computer_science
#       return f"Percentage of {self.student_name} is  {sum2*100 / 500}"
#
# Nitish = Students ("Nitish", 82, 86, 89, 87, 77)
# Priya = Students ("Priya", 96, 97, 79, 89, 75)
# Tanya = Students ("Tanya", 88, 81, 91, 83, 88)
# Himanshu = Students ("Himanshu", 87, 82, 88, 90, 95)
# Gunnu = Students ("Garamjeet", 00, 00, 00, 00, 00)
#
# print(Nitish.printscore_card())
# print(Priya.printscore_card())
# print (Tanya.printscore_card())
# print (Himanshu.printscore_card())
# print (Gunnu.printscore_card())
#
# print(Nitish.__add__())
# print(Priya.__add__())
# print(Tanya.__add__())
# print(Himanshu.__add__())
# print(Gunnu.__add__())
#
# print(Nitish.percentage())
# print(Priya.percentage())
# print(Tanya.percentage())
# print(Himanshu.percentage())
# print(Gunnu.percentage())

class Students():
    num = 100

    def __init__(self,a,b):
        self.first = a
        self.second = b

    def prap(self):
        return self.first + self.second + Students.num

class champaklal():
    paisa = 1088

    def __init__(self,j,k):
        self.pehla = j
        self.doosra = k

    def kyabe(self):
        return self.pehla + self.doosra + champaklal.paisa