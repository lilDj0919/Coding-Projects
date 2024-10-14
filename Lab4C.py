# Class: 1321L
# Section: BJD
# Term: Fall 2024
# Instructor: Tejaswini Karanan
# Name: D'Aveon Jackson

def main():
    balance = 1000
    while True:
        # Print the welcome message and menu options
        print("Welcome!")
        print("You have $1000 in your account.")
        print("0 - Make a deposit")
        print("1 - Make a withdrawal")
        print("2 -  Display account value")


        # Get user input for menu choice
        choice = input("Please make a selection: ")

        if choice == '0':
            # Deposit money
            amount = float(input("How much would you like to deposit?: "))
            balance += amount
            print(f"Deposit successful! Your new balance is ${balance:.2f}.")

        elif choice == '1':
            # Withdraw money
            amount = float(input("How much would you like to withdraw?: "))
            if amount > balance:
                print("Insufficient funds!")
            else:
                balance -= amount
                print(f"Withdrawal successful! Your current balance is ${balance:.2f}.")

        elif choice == '2':
            # Check balance
            print(f"Your current balance is ${balance:.2f}.")

        else:
            # Invalid choice
            print("Invalid choice. Please enter a number between 0 and 2.")

        # Ask if the user wants to return to the main menu
        continue_choice = input("Would you like to return to the main menu (Y/N)?: ")
        if continue_choice.lower() != 'y':
            print("Thank you for banking with us!")
            break


# Run the main function
if __name__ == "__main__":
    main()
