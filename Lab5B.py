# Class: 1321L
# Section: BJD
# Term: Fall 2024
# Instructor: Tejaswini Karanan
# Name: D'Aveon Jackson

size = int(input("Please a value for the size: "))
print("This is the requested ", str(size) +"x"+str(size),"box:")
print(" ")
for i in range(size):
    print("*" * size)
print(" ")
print("The is the requested right-facing", str(size) +"x"+str(size), "box:")
print(" ")
num = 1
while num<= size:
    for i in range(size):
        print("*" * (size - int(size-(num))))
        num +=1
print(" ")
print("The is the requested left-facing", str(size) +"x"+str(size), "box:")
print(" ")
space = size - 1
num = 1
while num<= size:
    for i in range(size):
        print(" " * int(space), end=" ")
        space -= 1
        print("*" * (size - int(size-(num))))
        num +=1