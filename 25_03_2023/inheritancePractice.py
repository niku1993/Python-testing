class polygon:

    def __init__(self,length,number):
        self.anumber = length
        self.bnumber = number

    def perimeter (self):
        return f"perimeter of polygon is {self.anumber * self.bnumber}"

class triangle (polygon):

    def __init__(self):
        polygon.__init__(self,4,3)

    def perimeterTriangle (self):
        return f"perimeter of triangle is {self.anumber + self.bnumber}"

obj = triangle()
print (obj.perimeterTriangle())
print (obj.perimeter())