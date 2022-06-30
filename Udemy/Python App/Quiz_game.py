from doctest import OutputChecker


print("Welcome to my computer quiz")

play = input("Do you want to play? ")

if play != "yes":    
    quit()   # can also use if True instead of if play != "yes":

print("Okay! Let's play:)")

answer = input("What does CPU stand for? ")

if answer != "Central Processing Unit":
    quit()
print("Correct!")
