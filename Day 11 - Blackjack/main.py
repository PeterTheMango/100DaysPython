from art import logo
from random import choice

def clear():
    for i in range(1000):
        print('\n')
    return

def CompareScores(uScore: int, cScore: int):
    if uScore == cScore:
        return "It's a Draw!"
    elif cScore == 0:
        return "You Lose!"
    elif uScore == 0:
        return "You Win!"
    elif uScore > 21:
        return "You Lose! Your score has gone over 21."
    elif cScore > 21:
        return "You Win! The computer score has gone over 21."
    else:
        if cScore > uScore:
            return "You Lose! The computer has a higher score than you."
        else:
            return "You Win!, You have a higher score than the computer."

def DealCard(deck):
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    deck.append(choice(cards))
    return deck

def CalculateScore(cards: list):
    score = sum(cards)
    if cards[0] == 11 and cards[1] == 10 and len(cards) == 2:
        return 0
    if score > 21 and 11 in cards:
        for i in range(len(cards)):
            if cards[i] == 11:
                cards[i] = 1
        score = sum(cards)
    return score

def Blackjack():
    print(logo)

    cCards = []
    uCards = []

    for i in range(2):
        cCards = DealCard(cCards)
        uCards = DealCard(uCards)

    uScore = CalculateScore(uCards)
    cScore = CalculateScore(cCards)

    print(f"Your Cards: {str(uCards)}, Current Score: {uScore}")
    print(f"Computer's First Card: {cCards[0]}")

    if cScore == 0 or uScore > 21:
        print(CompareScores(uScore, cScore))
        return

    hit = input("Do you want to draw another card? Type 'y' or 'n': ").lower()
    while hit == "y":
        uCards = DealCard(uCards)
        uScore = CalculateScore(uCards)

        clear()
        print(logo)
        print(f"Your Cards: {str(uCards)}, Current Score: {uScore}")
        print(f"Computer's First Card: {cCards[0]}")

        if uScore > 21:
            print(CompareScores(uScore, cScore))
            return
        hit = input("Do you want to draw another card? Type 'y' or 'n': ").lower()
    
    while cScore < 17:
        cCards = DealCard(cCards)
        cScore = CalculateScore(cCards)
        if cScore == 0:
            print(CompareScores(uScore, cScore))
            return
            
    clear()
    print(logo)
    print(f"Your Cards: {str(uCards)}, Current Score: {uScore}")
    print(f"Computer's Cards: {str(cCards)}, Computer Score: {cScore}")
    print(f"Game Result: {CompareScores(uScore, cScore)}")

startGame = input("Do you want to play blackjack? Type 'y' or 'n': ").lower()
gameStarted = False

if startGame == 'y':
    gameStarted = True
    while gameStarted == True:
        clear()
        Blackjack()
        startGame = input("Do you want to play another game of blackjack? Type 'y' or 'n': ").lower()
        if startGame == 'y':
            gameStarted = True
        else:
            gameStarted = False
else:
    print('Exiting Now!')