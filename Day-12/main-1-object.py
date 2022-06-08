def can_vote(person):
    if person["age"] >= 18:
        print("Yes")
    else:
        print("No")


def print_info(person):
    print(f"name = {person['name']}")
    print(f"name = {person['age']}")


# data
person1 = {"name": "person1", "age": 30}
can_vote(person1)
print(person1)


# data
mobile = {"model": "iphone", "company": "apple"}
# can_vote(mobile)
