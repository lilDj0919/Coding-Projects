# Class: 1321L
# Section: BJD
# Term: Fall 2024
# Instructor: Tejaswini Karanan
# Name: D'Aveon Jackson

def main():
    print("Welcome to the Adventure Game!")

    while True:
       direction = input("Choose a direction to move (north, south, east, west) or type 'quit' to exit: ").strip().lower()

       if direction == 'quit':
           print("Thanks for playing!")
           break

       while direction not in ['north', 'south', 'east', 'west']:
            direction = input("Invalid direction. Please choose 'north', 'south', 'east', or 'west': ").strip().lower()


       if direction == 'north':
            print("You move north and find a river.")
            next_action = input("Do you want to 'swim' or 'build a raft'?").strip().lower()
            if next_action == 'swim':
                print("You swim across the river and find a hidden treasure.")
            elif next_action == 'build a raft':
                print("You build a raft and safely float across the river.")
            else:
                print("Invalid action. You hesitate and end up on the riverbank.")

       elif direction == 'south':
            print("You move south and discover a dense forest.")
            next_action = input("Do you want to 'climb a tree' or 'walk deeper into the forest'? ").strip().lower()
            if next_action == 'climb a tree':
                print("You climb the tree and spot a beautiful view of the forest.")
            elif next_action == 'walk deeper':
                print("You walk deeper into the forest and encounter a friendly a friendly deer. ")
            else:
                print("Invalid action. You get lost in the forest.")
       elif direction == 'east':
            print("You move east and encounter a mountain.")
            next_action = input("Do you want to 'climb the mountain' or 'go around it'? ").strip().lower()
            if next_action == 'climb the mountain':
                print("You climb the mountain and enjoy a breathtaking view from the top.")
            elif next_action == 'go around':
                print("You go around the mountain and discover a hidden valley.")
            else:
                print("Invalid action. You sit and ponder your next move.")
       elif direction == 'west':
            print("You move west and stumble upon a cave.")
            next_action = input("Do you want to 'enter the cave' or 'walk past it'? ").strip().lower()
            if next_action == 'enter the cave':
                print("You enter the cave and find a sleeping dragon. ")
            elif next_action == 'walk past':
                print("You walk past the cave and find a treasure chest. ")
            else:
                print("Invalid action. You hesitate at the cave entrance. ")

if __name__ == "__main__":
    main()















