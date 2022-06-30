from atexit import register
import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"] #options [0] = rock

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break #break out of while loop. Therfore, end program.
        
    if user_input not in options:
        continue #ask to type again
    
    random_number = random.randint(0, 2)
    # rock = 0, paper = 1, scissors = 2.
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")
    
    if user_input == "rock" and computer_pick == "scissors":
    
        print("You won!")
        user_wins += 1 
    
    

print("Goodbye!")


    
    
    
    