# empty class
class Person:
    pass


# instantiation: creating an object of a class
# reference = object
person = Person()

# object
# collection of key-value pairs
# keys => attributes
print(person.__dict__)

# add a new attribute
setattr(person, "name", "person1")
setattr(person, "address", "pune")
setattr(person, "age", 40)

# print(person.__dict__)

# getting value an attribute name
print(f"name = {getattr(person, 'name')}")
print(f"address = {getattr(person, 'address')}")
print(f"age = {getattr(person, 'age')}")


# create another object
person2 = Person()
print(person2.__dict__)

setattr(person2, "first_name", "person2")
setattr(person2, "full_address", "mumbai")
setattr(person2, "person_age", 10)
setattr(person2, "email", "person2@test.com")
setattr(person2, "mobile", "+91344565")

print(person2.__dict__)

print(f"name = {getattr(person2, 'first_name')}")
print(f"address = {getattr(person2, 'full_address')}")
print(f"age = {getattr(person2, 'person_age')}")

