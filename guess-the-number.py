# Guess the number Game
secretNumber = 9
guessCount = 0
guessLimit = 3
while guessCount < guessLimit:
    guess = int(input('Guess the number: '))
    if guess == secretNumber:
        print("You won!")
        break
    else:
        guessCount += 1
        if guessCount == 3:
            print("Game over")
        else:
            print("Try again")