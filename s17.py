#
#
# student = {}
#
# yassin = copy(student)
# nima = student

# yassin["name"] = "yassin"
#
# nima["name"] = "nima"
#
# print(yassin)
# print(nima)


class Student:
    def __init__(self, name: str,last_name :str , score: int) -> None:
        self.name = name
        self.last_name = last_name
        self.score = score
    #
    def __str__(self):
        return f'mr.{self.name}'
    #
    def len(self) -> int:
        return 87879786645576

    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Student) and self.name == __o.name
    def greeting(self):
        print(self)
        print(type(self))
        print(f"Hello {self.name}! {self.last_name} your score is {self.score}")






# nima = Student("Nima","x",100)
# print(nima.last_name)
#
# nima.greeting()
#
# shirin = Student("Shirin",'y',50)
#
# shirin.greeting()



a = Student("milad", "sole", 330)
a2 = Student("milad", "sole", 2)


print(a.__str__())
print(a == a2)
print(a is a2)

print(a.len())


