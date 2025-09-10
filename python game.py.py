# Number Guessing Game
# Python 3.8+

import random

def play_game():
    print("\nWelcome to Number Guessing!")
    # choose difficulty
    difficulties = {"easy": 15, "medium": 10, "hard": 5}
    while True:
        choice = input("Choose difficulty (easy / medium / hard): ").strip().lower()
        if choice in difficulties:
            attempts_left = difficulties[choice]
            break
        print("Type 'easy', 'medium' or 'hard'.")

    secret = random.randint(1, 100)
    print("I'm thinking of a number between 1 and 100.")
    print(f"You have {attempts_left} attempts. Good luck!")

    while attempts_left > 0:
        guess = input(f"\nAttempt {difficulties[choice] - attempts_left + 1} — your guess: ").strip()
        if not guess.isdigit():
            print("Enter a whole number between 1 and 100.")
            continue

        guess = int(guess)
        if guess < 1 or guess > 100:
            print("Number must be between 1 and 100.")
            continue

        if guess == secret:
            print(f"Nice! {guess} is correct. You win!")
            break
        elif guess < secret:
            print("Too low.")
        else:
            print("Too high.")

        attempts_left -= 1
        print(f"Attempts left: {attempts_left}")

    else:
        print(f"\nOut of attempts — the number was {secret}.")

def main():
    while True:
        play_game()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != 'y':
            print("Thanks for playing. Bye!")
            break

if __name__ == "__main__":
    main()
