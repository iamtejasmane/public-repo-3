# decorators
def execute(function):
    print("inside execute ")
    print(f"function = {function}, type = {type(function)}")

    def inner(p1, p2):
        print("-" * 40)
        print(function(p1, p2))
        print(f"-" * 40)

    return inner


@execute
def add(p1, p2):
    return f"{p1} + {p2} = {p1 + p2}"


@execute
def subtract(p1, p2):
    return f"{p1} - {p2} = {p1 - p2}"


@execute
def multiply(p1, p2):
    return f"{p1} * {p2} = {p1 * p2}"


# ref_add = execute(add)
# ref_add(10, 20)

# ref_subtract = execute(subtract)
# ref_subtract(10, 20)

# ref_multiply = execute(multiply)
# ref_multiply(10, 20)

add(10, 20)

subtract(10, 20)

multiply(10, 20)
