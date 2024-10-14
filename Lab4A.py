# Class: 1321L
# Section: BJD
# Term: Fall 2024
# Instructor: Tejaswini Karanan
# Name: D'Aveon Jackson

Exam_score = float(input("Enter the score of your exam: "))
Exam_score = round(Exam_score)

if 98<= Exam_score<= 100:
    print(" Letter grade is: A+ ")

elif 95<= Exam_score <= 97:
    print(" Letter grade is: A ")

elif 92<= Exam_score <= 94:
    print(" Letter grade is: A-")

elif 89<= Exam_score <= 91:
    print(" Letter grade is: B+")

elif 86<= Exam_score <= 88:
    print(" Letter grade is: B")

elif 83<= Exam_score <= 85:
    print(" Letter grade is: B-")

elif 80<= Exam_score <= 82:
    print(" Letter grade is: C+")

elif 77<= Exam_score <= 79:
    print(" Letter grade is: C-")

elif 71<= Exam_score <= 73:
    print(" Letter grade is: D+")

elif 68<= Exam_score <= 70:
    print(" Letter grade is: D")

elif 65<= Exam_score <= 97:
    print(" Letter grade is: D-")

else:
    print(" Letter grade is: F")

