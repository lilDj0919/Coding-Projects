# Class: 1321L
# Section: BJD
# Term: Fall 2024
# Instructor: Tejaswini Karanan
# Name: D'Aveon Jackson

weight = int(input("Enter your weight in kilograms:"))
height = float(input("Enter your height in centimeters:"))/100
BMI = round((weight)/(height**2), 1)
print ("Your BMI is: " + str(BMI))

if BMI < 18.5:
    print ("You are classified as: 1 weight ")

elif 18.5 <= BMI <= 24.9:
    print("You are classified as: 2 weight ")

elif 25 <= BMI <= 29.9:
    print("You are classified as: 3 weight ")

else:
    print("You are classified as: 4 weight ")