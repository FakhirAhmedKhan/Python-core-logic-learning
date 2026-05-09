import random

# --- Number Guessing Game ---
# A simple game where you try to guess a secret number.

def play_game():
    """
    Main game logic for a single round of guessing.
    """
    # 1. Computer selects a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False

    print("\nI have selected a number between 1 and 100.")
    print("Can you guess it?")

    # 2. Game loop
    while not guessed_correctly:
        try:
            # Ask for user input
            user_guess = int(input("\nEnter your guess: "))
            attempts += 1

            # 3. Check the guess
            if user_guess < secret_number:
                print("Too low! Try again.")
            elif user_guess > secret_number:
                print("Too high! Try again.")
            else:
                # Success message
                print(f"\nCONGRATULATIONS! You found the number {secret_number}!")
                print(f"It took you {attempts} attempts.")
                guessed_correctly = True
        
        except ValueError:
            print("Invalid input! Please enter a whole number.")

def main():
    print("="*30)
    print("  NUMBER GUESSING GAME  ")
    print("="*30)

    while True:
        play_game()
        
        # 4. Ask user if they want to play again
        play_again = input("\nDo you want to play again? (yes/no): ").lower().strip()
        
        if play_again != "yes" and play_again != "y":
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()
