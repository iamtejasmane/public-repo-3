"""
List slicing returns a new list from the existing list.
Syntax : Lst[ start_index : end_index : index_jump ]
If Lst is a list, then the above expression returns the portion of the list
from start_index to end_index, at a step size index_jump.
"""
# imp : end_index does not consider the upper bound


def function1():
    # Initialize list
    lst = [50, 70, 30, 20, 90, 10, 80]

    # Display list
    print(f"positive list = {lst[::]}")
    print(f"negative list = {lst[-7::1]}")
    # print(f"list = {lst[1:5]}")
    print(f"lst = {lst[3:9:2]}")
    print(f"lst = {lst[::]}")  # slice step can not be zero

    print(lst[10::2])  # limit exceed gives empty list
    print(lst[1:1:1])  # empty list
    print(lst[-1:-1:-1])  # empty list
    print(lst[:0:])  # empty list



function1()


