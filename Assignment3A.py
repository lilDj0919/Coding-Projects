# Class: 1321L
# Section: BJD
# Term: Fall 2024
# Instructor: Tejaswini Karanan
# Name: D'Aveon Jackson

num_rows = int(input("Enter a positive integer: "))

current_number = 1

for i in range(1, num_rows + 1):
    row_numbers = []
    for j in range(i):
        row_numbers.append(str(current_number))
        current_number += 1
    print(" ".join(row_numbers))

