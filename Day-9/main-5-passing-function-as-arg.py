def add(p1, p2):
    print(f"addition = {p1 + p2}")


def subtract(p1, p2):
    print(f"subtraction = {p1 - p2}")


def multiply(p1, p2):
    print(f"multiplication = {p1 * p2}")


def divide(p1, p2):
    print(f"division = {p1 / p2}")


def execute(function):
    # function = add
    print(f"function = {function}")
    function(10, 20)
    function(30, 40)
    function(70, 80)
    function(90, 100)


execute(add)
execute(subtract)
execute(multiply)
execute(divide)
