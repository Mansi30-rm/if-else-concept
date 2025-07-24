import random

computer = random.randint(1,100)

print("Welcome to the Number Guessing Game")
print("I'm thinking number between 1 to 100")

while True:
    user_input = int(input("Enter a number between 1 to 100: "))

    if user_input == computer:
        print("YOU WIN!")
        break;

    elif user_input > computer:
        print("number is to big! Try again")
    
    elif user_input < computer:
        print("number is to small! Try again")
    
    else:
        print("Invaild number")