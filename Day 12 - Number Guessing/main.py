from art import logo
from random import randint

HARD_LIVES = 5
EASY_LIVES = 10

def clear():
    for i in range(1000):
        print('\n')
    return

def GuessNumber(num, answer):
    if num != answer:
        return False
    else:
        return True

def PlayGame():
    print(logo)

    print("""Welcome Player! I am Grandmaster CP! I am currently thinking of a number between 1-100.
    
The objective of the game is to guess what number I am thinking of based on the results of your answer.""")

    mode = input("Choose your difficulty [EASY | HARD]: ").lower()

    while mode != "easy" and mode != "hard":
        print("ERROR: You have providede an invalid game difficulty.")
        mode = input("Choose your difficulty [EASY | HARD]: ").lower()

    if mode == "easy":
        userLives = EASY_LIVES
    else:
        userLives = HARD_LIVES

    answer = randint(1,100)
    print(f"[DEBUG] Your answer is: {answer}")
    while userLives > 0:
        print(f"Remaining Life Points: {userLives}")
        guess = input("Enter your guess: ")
        while not guess.isnumeric():
            print("ERROR: Your guess must be a valid number.")
            guess = input("Enter your guess: ")
        guess = int(guess)
        result = GuessNumber(guess, answer)
        if not result:
            userLives -= 1
            if userLives == 0:
                print("You have run out of guesses! You have now lost.")
            else:
                if guess > answer:
                    print("I'm sorry but that's the wrong guess. You have now lost a life. Hint: Lower")
                else:
                    print("I'm sorry but that's the wrong guess. You have now lost a life. Hint: Higher")
        else:
            print("Congratulations! You have successfully guessed the number that I was thinking of.")
            userLives = 0


clear()

runningGame = False

start = input("Would you like to play guess the number? Type 'y' or 'n': ").lower()
while start != 'y' and start != 'n':
    print("Error: That is an invalid answer.")
    start = input("Would you like to play guess the number? Type 'y' or 'n': ").lower()

if start == "y":
    runningGame = True
else:
    runningGame = False

while runningGame:
    clear()
    PlayGame()
    start = input("Would you like to play another round? Type 'y' or 'n': ").lower()
    while start != 'y' and start != 'n':
        print("Error: That is an invalid answer.")
        start = input("Would you like to play another round? Type 'y' or 'n': ").lower()
    if start == "y":
        runningGame = True
    else:
        runningGame = False

print("Game Done! Exiting Now!")
