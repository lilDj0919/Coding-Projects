# Class: 1321L
# Section: BJD
# Term: Fall 2024
# Instructor: Tejaswini Karanan
# Name: D'Aveon Jackson

smallsandwiches = int(input("Enter the number of small sandwiches: "))
mediumsandwiches = int(input("Enter the number of medium sandwiches: "))
largesandwiches = int(input("Enter the number of large sandwiches: "))
extralargersandwiches = int(input("Enter the number of extra-large sandwiches: "))

print("You've entered " + str(smallsandwiches) + " small sandwiches.")
print("You've entered " + str(mediumsandwiches) + " medium sandwiches.")
print("You've entered " + str(largesandwiches) + " large sandwiches. ")
print("You've entered" + str(extralargersandwiches) + " extra-large sandwiches.")
smallcooktime = 30
mediumcooktime = 60
largecooktime = 75
extralargecooktime = 135
smalltotalseconds = smallcooktime * smallsandwiches
minutes = int((smallsandwiches * smallcooktime + mediumsandwiches * mediumcooktime + largesandwiches * largecooktime
               + extralargersandwiches * extralargecooktime) / 60)
seconds = (smallsandwiches * smallcooktime + mediumsandwiches * mediumcooktime + largesandwiches * largecooktime
               + extralargersandwiches * extralargecooktime) % 60

print("\nTotal cooking time is " + str(minutes) + " minutes and " + str(seconds) + " seconds.")
