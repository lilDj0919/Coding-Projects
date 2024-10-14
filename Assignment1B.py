# Class: 1321L
# Section: BJD
# Term: Fall 2024
# Instructor: Tejaswini Karanan
# Name: D'Aveon Jackson


P = int(input("Enter the loan amount: "))
r = float(input("Enter the annual interest rate (in %) : "))/1200
n = int(input("Enter the loan term (in years): "))*12
part = (1+r)**n
top = P * r * part
bottom = part - 1
answer = top/bottom
print("Your monthly payment is: " + str(round(answer, 2)))