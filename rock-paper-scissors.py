import random

user_wins = 0
computer_wins = 0

selection = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break
    
    if user_input not in selection:
        print("Invalid option")
        continue

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2

    computer_selection = selection[random_number]
    print(f"Computer selected {computer_selection}")

    if user_input == "rock" and computer_selection == "scissors":
        print("You won!")
        user_wins += 1
    elif user_input == "paper" and computer_selection == "rock":
        print("You won!")
        user_wins += 1
    elif user_input == "scissors" and computer_selection == "paper":
        print("You won!")
        user_wins += 1
    elif user_input == computer_selection:
        print("It's a tie!")
    else:
        print("You lost!")
        computer_wins += 1

print("Game Over")
print(f"Final Score - User: {user_wins} / Computer: {computer_wins}")