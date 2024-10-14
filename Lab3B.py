# Class: 1321L
# Section: BJD
# Term: Fall 2024
# Instructor: Tejaswini Karanan
# Name: D'Aveon Jackson

Course1hours = int(input("Course 1 hours: "))
Gradeforcourse1 = int(input("Grade for course 1: "))
Course2hours = int(input("Course 2 hours: "))
Gradeforcourse2 = int(input("Grade for course 2: "))
Course3hours = int(input("Course 3 hours: "))
Gradeforcourse3 = int(input("Grade for course 3:"))
Course4hours = int(input("Course 4 hours: "))
Gradeforcourse4 = int(input("Grade for course 4: "))
quality1 = Course1hours * Gradeforcourse1
quality2 = Course2hours * Gradeforcourse2
quality3 = Course3hours * Gradeforcourse3
quality4 = Course4hours * Gradeforcourse4
totalqualitypoints = quality1 + quality2 + quality3 + quality4
coursehours = Course1hours + Course2hours + Course3hours + Course4hours
print("Total hours: " + str(coursehours))
print("Total quality points: " + str(totalqualitypoints))
gpa = round(float(totalqualitypoints / coursehours), 2)
print("Your GPA for this semester is " + str(gpa))

