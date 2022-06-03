# functions

def empty_function():
    pass


# defining a function
# parameterless function
def function1():
    print("inside fun 1")
    print("this is the func body")


# function call
# function1()


# function definition
# void function2(int param) {}
# function2("10");
# parameterized function
def function2(param):
    # param = 10 -> int
    # param = 10.56 -> float
    # param = "steve" -> str
    # param = True -> bool
    print("inside function 2")
    print(f"param = {param}, type = {type(param)}")

# int
# function2(10)

# float
# function2(10.56)

# str
# function2("steve")

# bool
# function2(True)


# parameterized function
def add(p1, p2):
    """
    this function will add two parameters
    :param p1: integer first argument
    :param p2: integer second parameter
    :return: nothing
    """
    print("inside add function")
    addition = p1 + p2
    print(f"addition = {addition}")


# dunder doc
# print(add.__doc__)
# add(10, 20)
# add("hello", "python")
# add(10.40, 45.7)


def function3():
    """
    documentation string (docstring)
    this is a test function
    :return: nothing
    """
    print("inside function3")


# function3()
# print(function3.__doc__)

def multiply(p1, p2):
    """
       multiply two parameters
       :param p1: int
       :param p2: int
       :return: multiplication of two parameters
       """
    multiplication = p1 * p2
    return multiplication


answer = multiply(40, 60)
print(f"answer = {answer}, data type = {type(answer)}")


def function4():
    print("inside func4")


value = function4()
print(value)  # None
