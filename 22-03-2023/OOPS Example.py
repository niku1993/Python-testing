#class Student:
 #   pass

#harry = Student ()
#larry = Student ()

#harry.name = 'Harry'
#harry.std = 12
#harry.section = 1
#larry.std = 9
#larry.subjects = ['hindi','physics']
#print (harry.std, larry.subjects)

class Employee:
    number_of_leaves = 8
    pass
harry=Employee()

rohan=Employee()

harry.name = 'Harry'
harry.role = 'Instructor'
harry.salary = 455

rohan.name = 'Rohan'
rohan.salary = 121
rohan.role = 'Student'

print (Employee.number_of_leaves)
rohan.number_of_leaves=9
print (rohan.number_of_leaves)