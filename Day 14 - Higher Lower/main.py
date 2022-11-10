from random import choice
from art import logo, vs
from game_data import data

def clear():
    for i in range(1000):
        print('\n')

def CorrectAnswer(uAnswer: int, sAnswer: int):
    return uAnswer > sAnswer       

def PlayGame():

    points = 0
    gameData = data.copy()

    print(logo)
    print("Welcome to Higher or Lower!\n\nYour objective is to correctly guess which choice has more followers.\n\nA correct answer will give you a point, while a wrong answer will end the game.\n")

    choice1 = choice(gameData)
    gameData.remove(choice1)

    result = True

    while result and len(gameData) > 0:
        print(f"\nYour Current Score: {points}\n")

        choice2 = choice(gameData)
        gameData.remove(choice2)

        print("[ Choice A ]", choice1["name"] + ",", choice1["description"] + ",", "from", choice1["country"])
        print(vs + '\n')
        print("[ Choice B ]", choice2["name"] + ",", choice2["description"] + ",", "from", choice2["country"])

        uAnswer = input("Which has more followers? 'A' or 'B': ").lower()
        while not uAnswer == "a" and not uAnswer == "b":
            print("ERROR: Enter a valid answer. [A | B]")
            uAnswer = input("Which has more followers? 'A' or 'B': ").lower()
        if uAnswer == "a":
            result = CorrectAnswer(choice1["follower_count"], choice2["follower_count"])
        else:
            result = CorrectAnswer(choice2["follower_count"], choice1["follower_count"])
            choice1 = choice2

        if result:
            print("That's the correct answer!")
            points += 1
        else:
            print("That's wrong! You have now lost.")

clear()

startGame = input("Do you want to play higher or lower? Type 'y' or 'n': ").lower()

while startGame == 'y':
    clear()
    PlayGame()
    startGame = input("Do you want to play another game? Type 'y' or 'n': ").lower()

print("Game Done! Thank you for playing.")