# Class: 1321L
# Section: BJD
# Term: Fall 2024
# Instructor: Tejaswini Karanan
# Name: D'Aveon Jackson

print("Welcome!")
x = float(input("Please input a number: "))
print("What would you like to do to this number: ")
print("0) Get the additive inverse of the number")
print("1) Get the reciprocal of the number")
print("2) Square the number")
print("3) Cube the number")
print("4) Exit the program")
choice = int(input())

match(choice):
    case 0:
        y = x * - 1
        print(f"The additive inverse of {x} is {y}" )
    case 1:
        if x == 0:
            print("Cannot divide by 0! ")
        else:
            y =  1/x
            print(f"The reciprocal of {x} is {y}")

    case 2:
        y = x * x
        print(f"The square of {x} is {y}")

    case 3:
        y = x * x * x
        print(f"The cube of {x} is {y}")

    case 4:
        print("Thank you, goodbye!")




