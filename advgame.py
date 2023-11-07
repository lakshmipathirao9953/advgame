
def start_game():
    print("Welcome to the Text Adventure Game!")
    print("You find yourself in a mysterious forest.")
    print("What will you do?")
    print("1. Go left")
    print("2. Go right")
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        print("You chose to go left.")

    elif choice == "2":
        print("You chose to go right.")
        
    else:
        print("Invalid choice. Please select 1 or 2.")
        start_game()


start_game()
