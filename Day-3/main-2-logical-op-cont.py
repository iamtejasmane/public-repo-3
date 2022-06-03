def can_vote(age):
    """ This function checks if person is eligible for voting
    or not"""

    if age >= 18:
        print("this person is eligible for voting")
    else:
        print("this person is not eligible for voting")


age_1 = 18
can_vote(age_1)

age_2 = 15
can_vote(age_2)

age_3 = 26
can_vote(age_3)
