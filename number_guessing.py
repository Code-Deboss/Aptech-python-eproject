import random

def number_guessing_game():
    number = random.randint(0, 999)
    attempts = 0
    max_attempts = 5
    
    print("**************************************************")
    print("                                                  ")
    print("        Welcome to the Number Guessing Game!")
    print("                                                  ")
    print("**************************************************\n")
    print("I have chosen a number between 0 and 999. You have", max_attempts, "attempts to guess it.\n")

    while attempts < max_attempts:
        print("--------------------------------------------------")
        print("Attempt:", attempts+1)
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess == number:
            print("Congratulations! You guessed the correct number in", attempts, "attempts!\n")
            return
        elif guess < number:
            print("Wrong guess! The number is greater than", guess)
        else:
            print("Wrong guess! The number is smaller than", guess)

    print("\n**************************************************")
    print("                Game Over!")
    print("**************************************************\n")
    print("You ran out of attempts. The number was:", number)

number_guessing_game()
