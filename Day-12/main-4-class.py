class Car:

    # method
    # self: current object on which the method is called
    def print_info(self):
        print(f"model = {self.model}")
        print(f"company = {self.company}")


c1 = Car()
print(Car.__dict__)
print(c1.__dict__)

# adding attributes
c1.model = 'XUV700'
c1.company = 'Mahindra'

# Car.print_info(c1)
c1.print_info()


c2 = Car()

c2.model = "i10"
c2.company = "hyundai"


c2.print_info()
