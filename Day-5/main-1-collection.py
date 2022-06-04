def function1():
    # empty list
    list_1 = []
    print(list_1)
    print(f"type of list_1 = {type(list_1)}")

    # empty list
    list_2 = list()
    print(list_2)
    print(f"type of list_2 = {type(list_2)}")

    # list with only one item
    list_3 = [10]
    print(list_3)
    print(f"type of list_3 = {type(list_3)}")

    # list with only one item
    list_3 = list([10])
    print(list_3)
    print(f"type of list_3 = {type(list_3)}")


# function1()


def function2():
    list_1 = [10, 20, 30, 40, 50]

    # iterating using for in loop
    for value in list_1:
        print(value)

    print("-*-" * 20)
    
    # iterating using traditional for loop
    index_position = list(range(len(list_1)))
    for index in index_position:
        print(list_1[index])


function2()
