# Table of any number input using Loop

"""
a=int(input("Enter Value: "))
b=1
while b<=10:
    print (a * b)
    b = b + 1
"""

# Table of any number input using OOPS
class Table:

    def __init__(self,number):
        self.anumber=number

    def cal(self):
        b = 1
        while b<=10:
            print (self.anumber * b)
            b = b + 1
            # return "10"

Number =int(input("Enter Value: "))
calculate=Table(Number)

calculate.cal()