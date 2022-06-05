def function1():
    numbers = [10, 20, 30, 40, 50]
    print(numbers)

    numbers.append(60)
    print(numbers)

    numbers.insert(3, 70)  # here 3 is the position not index
    print(numbers)

    numbers.pop()
    print(numbers)

    numbers.pop(2)  # here 2 is the index
    print(numbers)

    numbers.remove(20) # here it is a value
    print(numbers)


# function1()


def function2():
    numbers = [10, 30, 10, 50, 50, 70, 60, 20, 30, 40, 50]

    count_50 = numbers.count(50)
    print(f"50 repeated {count_50} times")

    index_70 = numbers.count(70)
    print(f"50 appears at {index_70} index")

    numbers_reverse = numbers.copy()
    numbers_reverse.reverse()
    print(f"reversed list = {numbers_reverse}")

    numbers_sort_asc = numbers.copy()
    numbers_sort_asc.sort()
    print(f"sorted list ascending order = {numbers_sort_asc}")

    numbers_sort_desc = numbers.copy()
    numbers_sort_desc.sort(reverse=True)
    print(f"sorted list descending order = {numbers_sort_desc}")


# function2()


def function3():
    #          0   1   2   3   4   5   6   7   8   9
    numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    #         -10  -9  -8  -7  -6  -5  -4  -3  -2   -1

    # positive
    print(f"value at first position = {numbers[0]}")
    print(f"value at last position = {len(numbers) - 1}")

    # negative
    print(f"value at first position = {numbers[-len(numbers)]}")
    print(f"value at last position = {numbers[-1]}")


function3()