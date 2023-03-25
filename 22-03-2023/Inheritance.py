from practice import Students, champaklal


class Inher(Students, champaklal):
    num2 = 200

    def __init__(self):
        super(Inher,self).__init__(1,2)
        champaklal.__init__(self, 7, 9)

    def Data(self):
        return self.num + self.num2 + self.paisa + self.prap() + self.kyabe()


# print(issubclass(Inher,Students))
# print(issubclass(Students,Inher))

Obj1=Students(1,2)
obj = Inher()
# print(isinstance(obj,Students))

print(obj.Data())
