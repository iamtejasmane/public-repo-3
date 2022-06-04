num = 100  # initialization
print(f"num = {num}, type = {type(num)}")

num2 = num  # initialization
print(f"num2 = {num2}, type = {type(num2)}")

num = 300  # assignment

print(f"num = {num}, type = {type(num)}")
print(f"num2 = {num2}, type = {type(num2)}")


def function1():
    print("inside function1")


print(f"function1 = {function1}")
print(f"type of function1 = {type(function1)}")

# function alias
# another name given to existing function
# variable to a function
my_function = function1
print(f"my_function = {my_function}")
print(f"type of my_function = {type(my_function)}")

function1()
my_function()

myFunction2 = function1
print(f"myFunction2 = {myFunction2}")

myFunction3 = function1
print(f"myFunction3 = {myFunction3}")

