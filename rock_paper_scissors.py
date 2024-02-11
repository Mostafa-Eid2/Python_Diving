import random

user_wins = 0
com_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break
            
    if user_input not in options:
        print("invalid input")
        continue
    
    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print("computer picked", computer_pick + ".")
    
    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1
        
    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1
        
    elif user_input == computer_pick:
        print("Draw! try again.")
        
    else:
        print("You lost!")
        com_wins += 1
        
print("You won", user_wins, "times.")
print("The computer won", com_wins, "times.")
print("Goodbye!")
