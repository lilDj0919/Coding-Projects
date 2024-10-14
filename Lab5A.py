# Class: 1321L
# Section: BJD
# Term: Fall 2024
# Instructor: Tejaswini Karanan
# Name: D'Aveon Jackson

print("Please enter 10 numbers and this program will display the largest.")
x = 0

for i in range(1,11):
    num = int(input(f"Please enter number {i}:"))

    if x < num:
        x = num
print(" ")
print("The largest number was ", str (x))



