# Class: 1321L
# Section: BJD
# Term: Fall 2024
# Instructor: Tejaswini Karanan
# Name: D'Aveon Jackson

from MyMath import my_max, my_min, my_avg

def main():
    num_one = float(input("Enter number 1: "))
    num_two = float(input("Enter number 2: "))

    max_value = my_max(num_one, num_two)
    min_value = my_min(num_one, num_two)
    avg_value = my_avg(num_one, num_two)

    print(f"The maximum of {num_one} and {num_two} is: {max_value}")
    print(f"The minimum of {num_one} and {num_two} is: {min_value}")
    print(f"The average of {num_one} and {num_two} is: {avg_value}")

if __name__ == "__main__":
    main()
