# logical operators

# and => &&
# true and true => true
# true and false => false
# false and true => false
# false and false => false

age = 70

# age > 20 and age < 60
# if() {
#   code here
# }

if (age > 20) and (age < 60):
    print("inside if block")
    print("valid age for an employee")
else:
    print("inside the else block")
    print("invalid age for an employee")

print("this is out of the if else block")

# or => ||

if (age > 25) or (age < 60):
    print("inside if block")
    print("valid age for an employee")
else:
    print("inside the else block")
    print("invalid age for an employee")