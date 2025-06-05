import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Generate random number
    secret_number = random.randint(1, 100)
    attempts = 7
    
    for attempt in range(1, attempts + 1):
        while True:
            try:
                guess = int(input(f"Attempt {attempt} of {attempts}. Make a guess: "))
                if 1 <= guess <= 100:
                    break
                else:
                    print("Please enter a number between 1 and 100.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
        
        if guess < secret_number:
            print("Too low.")
        elif guess > secret_number:
            print("Too high.")
        else:
            print(f"Congratulations! You guessed the number in {attempt} attempts!")
            break
    else:
        print(f"Sorry, you ran out of attempts. The number was {secret_number}.")

if __name__ == "__main__":
    number_guessing_game()

