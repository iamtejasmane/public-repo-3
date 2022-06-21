# base class
class Person:
    def __init__(self):
        print("base class constructor")
        self.name = ''
        self.address = ''
        self.age = 0

    def print_person_info(self):
        print("-- base class --")
        print(f"name = {self.name}")
        print(f"address = {self.address}")
        print(f"age = {self.age}")


# derived class
class Employee (Person):
    # derived class object getting initialized
    def __init__(self):
        # base class object getting initialized within derived class object
        print("derived class constructor")
        Person.__init__(self)
        self.id = 0
        self.company = ''


p1 = Person()
p1.print_person_info()


e1 = Employee()
# e1.print_person_info()

e2 = Employee()
# e2.print_person_info()

print(p1.__dict__)
print(e1.__dict__)
print(e2.__dict__)
