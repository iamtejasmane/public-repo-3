def function1():
    numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    numbers_slice = []

    # star: 2
    # stop: 5
    # position = [2, 3, 4, 5]
    position = range(2, 6)
    for index in position:
        numbers_slice.append(numbers[index])

    print(numbers_slice)


# function1()


def function2():
    numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    # slicing (2, 3, 4, 5)
    print(numbers[2:6])

    # slicing (4, 5, 6, 7, 8)
    print(numbers[4:9])

    # 40, 50, 60, 70, 80, 90, 100
    print(numbers[3:])

    # 10, 20, 30, 40, 50
    print(numbers[0:5])

    # 10, 20, 30, 40, 50
    print(numbers[:5])

    # 10, 20, 30, 40, 50, 60, 70, 80, 90, 100
    print(numbers[0:10])

    # 10, 20, 30, 40, 50, 60, 70, 80, 90, 100
    print(numbers[0:])

    # 10, 20, 30, 40, 50, 60, 70, 80, 90, 100
    print(numbers[:10])

    # 10, 20, 30, 40, 50, 60, 70, 80, 90, 100
    print(numbers[:])

    # 10, 20, 30, 40, 50, 60, 70, 80, 90, 100
    print(numbers[0:100])

    # 10, 20, 30, 40, 50, 60, 70, 80, 90, 100
    print(numbers)


# function2()


def function3():
    numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    numbers_even = []
    for index in range(len(numbers)):
        if index % 2 == 0:
            print(index)
            numbers_even.append(numbers[index])

    print(numbers_even)


# function3()


def function4():
    numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    # values at even position
    print(numbers[0:10:2])

    # values at even position
    print(numbers[::2])

    # values at odd position
    print(numbers[1:10:2])

    # values at odd position
    print(numbers[1::2])

    # values
    # print(numbers[0:10:1])
    print(numbers[::])

    # reverse the values
    print(numbers[::-1])

    # copy of numbers list
    # numbers_1 = numbers.copy()
    # number_1 = numbers[:]
    # number_1 = numbers[::]


function4()

