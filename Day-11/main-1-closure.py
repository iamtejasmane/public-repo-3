def add(p1, p2):
    print(f"-" * 40)
    print("inside add")
    print(f"p1 = {p1}, p2 = {p2}")
    addition = p1 + p2
    print(f"addition = {addition}")
    print("-" * 40)


# add(20, 10)


def divide(p1, p2):
    print(f"-" * 40)
    print("inside divide")
    print(f"p1 = {p1}, p2 = {p2}")
    division = p1 / p2
    print(f"addition = {division}")
    print("-" * 40)


# divide(20, 0)


def log(function):
    print(f"function name = {function.__name__}")


log(add)
log(divide)
