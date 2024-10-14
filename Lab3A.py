# Class: 1321L
# Section: BJD
# Term: Fall 2024
# Instructor: Tejaswini Karanan
# Name: D'Aveon Jackson

Amount_owed = int(input("Amount owed: $"))
APR = float(input("APR:" ))
Monthly_percentage_rate = float(APR/12)
print(("Monthly percentage rate:") + str(round(Monthly_percentage_rate, 3)))
Minimum_payment =float(round(Amount_owed * (Monthly_percentage_rate/100), 2))
print(("Minimum payment: $") + str(Minimum_payment))



