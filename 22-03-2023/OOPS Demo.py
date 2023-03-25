#CLasses are user defined blueprint or prototype

class Calculator:
    num =100

    def __init__(self):
        print ('I am called automatically when object is created')

    def getData(self):
        print ("I am executing as method in class")

obj = Calculator()  #syntax to create objects in python
obj.getData()
print (obj.num)