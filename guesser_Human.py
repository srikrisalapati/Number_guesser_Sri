import random
import sys
# Game Instructions
print("Welcome to the exciting number guessing game")
print("Game Rules")
print("1. System pre choose a number between 1 and 100")
print("2. you will be asked to guess the number in fewer attempts")
print("3. follow the hints to guess the correct number")
print("4. Use the whole numbers between 1 and 100 only so that you won't waste your tries")
print("-----------------------------------------------------------------------------------")
# Taking the input

user_input = input("Ready to play the game press enter, Q to quite the game:")
if user_input.lower()=="q":
    exit()
user_input == ""
print("Starting the Game")
while True :
    sys_guess = random.randint(1, 100)
    # print("Random number choosen:" ,sys_guess )
    while True : 
        try :
            guesser_input = input("Guess the number between 1 and 100 or Q to quit the game:")
            if guesser_input.lower() == "q" :
                exit()
            guesser_number = int(guesser_input)    
            if guesser_number > sys_guess :
                print("your guess is too high")
            elif guesser_number < sys_guess :
                print("your guess is too low")
            elif guesser_number == sys_guess :
                print("your guess is right")
                break
        except ValueError:
            print("invalid input, Q to quit the game or enter a valide number")

    play_more=input("you would like to play the game again(yes/no)").lower()
    if play_more == "yes" or play_more == "y" :
        continue
    else :
        break


