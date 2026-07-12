class Dog:
    def __init__(self, name, ow_name):
        self.name = name
        self.ow_name = ow_name

    def print_name(self):
        print(self.name)
    def print_ow_name(self):
        print(self.ow_name)

    def change_ow_name(self, new_ow_name):
        self.ow_name = new_ow_name




# a= list()
a = [1,2,3] # list(1,2,3)
aa = {"user_id": 23}

jessy = Dog('Jessy', 'hamid')

jessy.print_name()
jessy.print_ow_name()

print("---------------")

jessy.change_ow_name('akbar')
jessy.print_name()
jessy.print_ow_name()


print("---------------")

petter = Dog('Peter', 'amir')
petter.print_name()
petter.print_ow_name()

class Student:
    def __init__(self, name: str,last_name :str , score: int) -> None:
        self.name = name
        self.last_name = last_name
        self.score = score



ali = Student('Ali', 'rezaei',score=10)


class User:
    def __init__(self, name: str, last_name: str,email: str, password: str) -> None:
        self.name = name
        self.last_name = last_name
        self.email = email
        self.password = password

    def show_info(self):
        print("name is : ",self.name)
        print("last name is :",self.last_name)
        print("email: ",self.email)
        print("password: ","*"*len(self.password))

    def __str__(self):
        return self.name

    def __len__(self):
        return len(self.last_name)

    def __eq__(self, __o: object) -> bool:
        return True






milad = User('milad','soleymani','soleymani.milad@gmail.com','12345678')

ali = User('ali','borhani','ali.bo@gmail.com','2323')

milad2 = milad
milad.show_info()

print(milad) # milad -> milad.__str__() -> stdout
print(ali)

print(len(milad))

print(milad is milad2)


class Animal:
    def __init__(self, name : str, age : int,sound: str) -> None:
        self.name = name
        self.age = age
        self.sound = sound

    def eat(self):
        return "eating"


class Dog(Animal):
    def __init__(self, name : str, age : int,sound: str,ow_name: str) -> None:
        super().__init__(name=name,sound=sound,age=age)
        self.ow_name = ow_name

    def bark(self):
        return "barking"


class GermanSheperd(Dog):
    def __init__(self, name : str, age : int,sound: str,ow_name: str) -> None:
        super().__init__(name=name,sound=sound,age=age)
        self.ow_name = ow_name

    def bark(self):
        return "barking"

a = Dog('petty',2676,'woof','radvin')

print(a.bark())
print(a.eat())

print(isinstance(a,Animal))
print(isinstance(a,Dog))