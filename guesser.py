import random
import sys # Import the sys module

# Game Initialization
print("Welcome to play this exciting number-guessing game")
print("Rules of the game:")
print("1. You will be asked to guess a number between 1 and 100")
print("2. If pick the right number, you win. Otherwise you get a chance to pick a number again with some hints")
print("3. Press Q to quit the game any time.")

# Wait for user to press Enter to start or Q to quit
start_input = input("Press Enter to start the game or Press Q to quit: ")

# Check if the user wants to quit at the start
if start_input.lower() == 'q':
    print("Quitting game...")
    sys.exit() # Exit the program

# Flag to indicate if the user wants to quit during the game
quit_game = False

# Outer loop to control playing again
while True:
    # The computer randomly picks a secret number within a certain range (e.g., between 1 and 100).
    secret_number = random.randint(1, 100)
    guesses = 0

    print("\nI have picked a new secret number!") # Message for a new game

    # The game continues until the player guesses the secret number.
    while True:
        try:
            # The player gets to guess the number.
            # Read input as string first to check for 'Q'
            guess_input = input("Enter your guess (between 1 and 100, or Q to quit): ")

            # Check if the user wants to quit during the game
            if guess_input.lower() == 'q':
                quit_game = True
                break # Break the inner loop

            # If not 'Q', try to convert to integer
            guess = int(guess_input)
            # The program might also count how many guesses it took.
            guesses += 1

            # The program tells the player if their guess is too high, too low, or correct.
            if guess < secret_number:
                print("Too low!")
            elif guess > secret_number:
                print("Too high!")
            else:
                print("Correct! You guessed the number in", guesses, "guesses.")
                break # Exit the inner loop when the guess is correct

        except ValueError:
            # Handle cases where input is not 'Q' and not a valid number
            print("Invalid input. Please enter a number or 'Q' to quit.")

    # Check the quit_game flag after the inner loop breaks
    if quit_game:
        break # Break the outer loop if user wants to quit

    # Ask user if they wish to play again
    play_again = input("Do you wish to play the game again? (yes/no): ").lower()

    if play_again == "yes" or play_again == "y":
        continue # Continue the outer loop to play again
    else:
        break # Exit the outer loop to quit the game

print("Thanks for playing!") # Message when the game ends