# Class: 1321L
# Section: BJD
# Term: Fall 2024
# Instructor: Tejaswini Karanan
# Name: D'Aveon Jackson

def isValid(width, height):

    return (width + height) > 30

def area(width, height):

    return width * height

def perimeter(width, height):

    return 2 * (width + height)

def main():
    while True:
        try:
            width = float(input("Enter width: "))
            height = float(input("Enter width: "))

            if isValid(width, height):
                rect_area = area(width, height)
                rect_perimeter = perimeter(width, height)

                print(f"This is a valid rectangle: ")
                print(f"Area: {rect_area}")
                print(f"Perimeter: {rect_perimeter}")

            else:
                print("This is an invalid rectangle")

        except ValueError:
            print("Enter valid numbers for width and height.")

        continue_program = input("Do you want to enter another rectangle? (yes/no): ").strip().lower()
        if continue_program != 'yes':
            break

if __name__ == "__main__":
    main()




