def function1():
    # list
    numbers_list = [10, 20, 30, 40, 50]
    print(f"numbers = {numbers_list}, type = {type(numbers_list)}")

    # tuple
    numbers_tuple = (10, 20, 30, 40, 50)
    print(f"numbers = {numbers_tuple}, type = {type(numbers_tuple)}")


# function1()


def function2():
    # empty list
    list_1 = []
    print(f"list_1 = {list_1}, type = {type(list_1)}")

    # empty list
    list_2 = list()
    print(f"list_2 = {list_2}, type = {type(list_2)}")

    # list with only one value
    list_3 = [10]
    print(f"list_3 = {list_3}, type = {type(list_3)}")

    # empty tuple
    tuple_1 = ()
    print(f"tuple_1 = {tuple_1}, type = {type(tuple_1)}")

    # empty tuple
    tuple_2 = tuple()
    print(f"tuple_2 = {tuple_2}, type = {type(tuple_2)}")

    print("-*-" * 30)

    # tuple with only one value consider as a single variable
    # tuple_3 is an int
    tuple_3 = (10)
    print(f"tuple_3 = {tuple_3}, type = {type(tuple_3)}")

    # tuple with only one value
    # tuple_4 is a str
    tuple_4 = ("india")
    print(f"tuple_4 = {tuple_4}, type = {type(tuple_4)}")

    # tuple with only one value
    tuple_5 = (10, )
    print(f"tuple_5 = {tuple_5}, type = {type(tuple_5)}")

    # tuple with only one value
    tuple_6 = ("india", )
    print(f"tuple_6 = {tuple_6}, type = {type(tuple_6)}")

    # tuple
    tuple_7 = (10, 20, 30, 40, 50)
    print(f"tuple_7 = {tuple_7}, type = {type(tuple_7)}")

    # tuple without parenthesis
    tuple_8 = 10, 20, 30, 40, 50
    print(f"tuple_8 = {tuple_8}, type = {type(tuple_8)}")


# function2()


def function3():
    # tuple
    numbers = (10, 20, 50, 60, 80, 10, 20, 30, 40, 50)

    # count of 50
    count_50 = numbers.count(50)
    print(f"50 appeared {count_50} times")

    # index position of 50
    position_50 = numbers.index(50)
    print(f"50 appeared at {position_50} position")


# function3()


def math_operations(p1, p2):
    addition = p1 + p2
    subtraction = p1 - p2
    division = p1 / p2
    multiplication = p1 * p2
    return addition, subtraction, division, multiplication


answers = math_operations(40, 20)
print(f"type of answers = {type(answers)}")
print(f"addition = {answers[0]}")
print(f"subtraction = {answers[1]}")
print(f"division = {answers[2]}")
print(f"multiplication = {answers[3]}")
