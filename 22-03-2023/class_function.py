class Employee :
    no_of_leaves = 8

    def printdetails (self):
        return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"

harry = Employee()
rohan = Employee ()

harry.name = 'Harry'
harry.salary = 455
harry.role = 'Instructor'

rohan.name = 'Rohan'
rohan.salary = 4554
rohan.role = 'Student'

print (rohan.printdetails ())
