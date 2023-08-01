import random

class NumberGuessingGame:
    def __init__(self):
        self.secret_number = random.randint(0, 999)
        self.max_attempts = 5
        self.attempts = 0

    def check_guess(self, guess):
        self.attempts += 1
        if guess == self.secret_number:
            return "Congratulations! You guessed the correct number in {} attempts!\n".format(self.attempts)
        elif guess < self.secret_number:
            return "Wrong guess! The number is greater than {}\n".format(guess)
        else:
            return "Wrong guess! The number is smaller than {}\n".format(guess)

class GameUI:
    def __init__(self):
        print("**************************************************")
        print("                                                  ")
        print("        Welcome to the Number Guessing Game!")
        print("                                                  ")
        print("**************************************************\n")

    def get_guess(self):
        try:
            return int(input("Enter your guess: "))
        except ValueError:
            print("\033[91mInvalid input! Please enter a valid number.\033[0m")
            return None

    def display_message(self, message):
        print(message)

    def display_game_over(self, secret_number):
        print("\n**************************************************")
        print("                Game Over!")
        print("**************************************************\n")
        print("You ran out of attempts. The number was:", secret_number)

def main():
    ui = GameUI()
    game = NumberGuessingGame()

    while game.attempts < game.max_attempts:
        ui.display_message("Attempt: {}".format(game.attempts + 1))
        guess = ui.get_guess()

        if guess is not None:
            result = game.check_guess(guess)
            ui.display_message(result)

            if "Congratulations!" in result:
                return

    ui.display_game_over(game.secret_number)

if __name__ == "__main__":
    main()
