# Class: 1321L
# Section: BJD
# Term: Fall 2024
# Instructor: Tejaswini Karanan
# Name: D'Aveon Jackson

age = float(input("Enter your age: "))
if 18<= age <=64:
    club = input("Are you a member of the cinema club (yes or no)? ")

    if club == "yes":
        print("Your ticket price is: $12")

    elif club != "yes":
        print("Your ticket price is: $15")

elif age<=12:
    print("Your ticket price is: $8")

elif 12<= age <=17:
    print("Your ticket price is: $10")

else:
    print("Your ticket price is: $10")