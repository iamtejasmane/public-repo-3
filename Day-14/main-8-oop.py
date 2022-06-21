class Person:
    def __init__(self, name, address, age):
        self.name = name
        self.address = address
        self.age = age

    def print_person_info(self):
        print(f"name = {self.name}")
        print(f"address = {self.address}")
        print(f"age = {self.age}")


class Employee(Person):
    def __init__(self, name, address, age, ID, company):
        Person.__init__(self, name, address, age)
        self.id = ID
        self.company = company


# p1 = Person('person1', 'pune', 20)
# p1.print_person_info()


e1 = Employee('employee1', 'pune', 35, 1, 'company1')
e1.print_person_info()