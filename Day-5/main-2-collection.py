def function1():
    # list
    list_1 = [10, 20, 30, 40, 50]
    # before appending
    print(list_1)
    # adding value 60 at the end of the list
    list_1.append(60)
    # after appending
    print(list_1)

    # append user input value
    str_value = input("Enter value : \n")
    # int conversion
    value = int(str_value)
    list_1.append(value)
    # final list
    print(list_1)


# function1()

def function2():
    # list
    list_1 = [10, 20, 30, 40, 50]

    print(list_1)

    # insert value 60 after 30 or insert value at the position 3
    list_1.insert(3, 60)

    print(list_1)

    # insert string into existing integer list
    list_1.append("a value 1")
    list_1.insert(2, "a value 2")
    print(list_1)


# function2()


def function3():
    # list
    list_1 = [10, 20, 30, 40, 50]
    print(list_1)

    # remove last value
    value = list_1.pop()
    print(f"list = {list_1}")
    print(f"removed value = {value}")


# function3()


def function4():
    # list
    list_1 = ["index", "usa", "uk", "china", "japan"]

    # remove china using the index from the list_1
    list_1.pop(3)

    print(list_1)


# function4()

def function5():
    # list
    list_1 = ["index", "usa", "uk", "china", "japan"]

    # remove china using value
    list_1.remove("china")

    print(list_1)


# function5()


def function6():
    # list
    list_1 = [10, 50, 20, 40, 50, 30, 50, 10, 30, 20]
    print(list_1)

    # removing value 30
    list_1.remove(30)
    print(list_1)

    # removing value 30
    list_1.remove(30)
    print(list_1)

    # removing value 30
    # list_1.remove(30)


# function6()


def function7():
    # list
    list_1 = [10, 50, 20, 40, 50, 30, 50, 10, 30, 20]
    print(list_1)

    # find occurrences of 30
    count_30 = list_1.count(30)
    print(f"30 repeated {count_30} times")

    # remove all the occurrences
    for index in range(count_30):
        list_1.remove(30)

    count_50 = list_1.count(50)
    print(f"50 repeated {count_50} times")

    for index in range(count_50):
        list_1.remove(50)

    print(list_1)


# function7()


def function8():
    # list
    fruits = ["apple", "banana", "orange", "jackfruit", "apple"]

    print(f"apple repeated {fruits.count('apple')} times")

    count_apple = fruits.count('apple')
    for index in range(count_apple):
        fruits.remove('apple')

    print(fruits)


# function8()


def function9():
    # list
    list_1 = [10, 50, 20, 40, 50, 30, 50, 10, 30, 20]

    print(f"50 repeat {list_1.count(50)} times")

    # position_50 = list_1.index(50)
    # print(f"50 appears at the position {position_50}")
    #
    # position_50 = list_1.index(50, 2)
    # print(f"50 appears at the position {position_50}")
    #
    # position_50 = list_1.index(50, 5)
    # print(f"50 appears at the position {position_50}")
    position = 0

    count_50 = list_1.count(50)
    for index in range(count_50):
        position_50 = list_1.index(50, position)
        print(f"50 appears at {position_50}")

        # search for 50 from the next position
        position = position_50 + 1


# function9()


def function10():
    # list
    list_1 = [10, 50, 20, 40, 50, 30, 50, 10, 30, 20]
    print(list_1)

    # create a copy of list_1
    list_1_sorted_asc = list_1.copy()

    print(list_1_sorted_asc)

    # inplace sort
    # modifies the original collection
    list_1_sorted_asc.sort()
    print(list_1_sorted_asc)

    # create a copy of list_1
    list_1_sorted_desc = list_1.copy()
    print(list_1_sorted_desc)
    # reverse a list
    list_1_sorted_desc.reverse()
    print(list_1_sorted_desc)
    # descending sort
    list_1_sorted_desc.sort(reverse=True)
    print(list_1_sorted_desc)


# function10()


def function11():
    # list
    list_1 = [10, 50, 20, 40, 50, 30, 50, 10, 30, 20]
    print(list_1)

    list_1.reverse()
    print(list_1)


# function11()


def function12():
    # list
    list_1 = [10, 50, 20, 40, 50, 30, 50, 10, 30, 20]
    print(list_1)

    # remove all the values
    list_1.clear()
    print(list_1)


# function12()


def function13():
    # list
    list_1 = [10, 20, 30, 40, 50]
    list_2 = [60, 70, 80, 90, 100]
    print(list_1)

    # append another list
    # list_1.append(list_2)
    list_1.extend(list_2)
    print(list_1)
    print(len(list_1))


# function13()


def function14():
    # list
    list_1 = [10, 20, 30, 40, 50]
    list_2 = [60, 70, 80, 90, 100]

    # list_3 = list_1.extend(list_2)
    # print(list_3)  # extend returns None

    # list_3 = list_1 + list_2
    # print(list_3)  # can extend the list with "+" operator

    list_3 = list_1.copy()
    list_3.extend(list_2)
    print(list_3)


function14()
