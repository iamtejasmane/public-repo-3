# collection
# Array or collection

# list          => []
# tuple         => ()
# set           => {}
# dictionary    => {}


def function1():
    # array of numbers (int)
    numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    print(numbers)
    print(f"type of numbers = {type(numbers)}")
    print(f"length of the list is = {len(numbers)}")

    # for in loop
    # for number in numbers:
    #     print(f"number = {number}")

    # using subscript operator
    print(f"value at 0th index = {numbers[0]}")
    print(f"value at 1th index = {numbers[1]}")
    print(f"value at 2th index = {numbers[2]}")
    print(f"value at 3th index = {numbers[3]}")
    print(f"value at 4th index = {numbers[4]}")

    # traditional for loop
    # for(int index = 0; index < 5; index++) { .. }

    # index_position = [0, 1, 2, 3, 4]
    # for index in index_position:
    #     print(f"value at index {index} = {numbers[index]}")

    # list of range 5 values [0, 1, 2, 3, 4]
    # index_position = list(range(1, 10))
    # index_position = list(range(len(numbers)))

    # index_position = [2, 3, 4, 5]
    # stop in range will NOT include the upper bound (2, 5)
    index_position = list(range(2, 6))
    print(f"index_positions = {index_position}")

    # traditional for loop
    for index in index_position:
        print(f"value at index {index} = {numbers[index]}")


function1()
