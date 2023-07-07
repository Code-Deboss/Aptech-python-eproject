import random

def number_guessing_game():
    number = random.randint(0, 999)
    attempts = 0
    max_attempts = 5
    
    print("Welcome to the Number Guessing Game!")
    print("I have chosen a number between 0 and 999. You have", max_attempts, "attempts to guess it.")

    while attempts < max_attempts:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess == number:
            print("Congratulations! You guessed the correct number in", attempts, "attempts!")
            return
        elif guess < number:
            print("Wrong guess! The number is greater than", guess)
        else:
            print("Wrong guess! The number is smaller than", guess)

    print("Game over! You ran out of attempts. The number was:", number)

number_guessing_game()