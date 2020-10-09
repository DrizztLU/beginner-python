import random

# Constants
# Prefixing using c for coding convention
cMaxAttempts = 10
cMinNumber = 1
cMaxNumber = 25
# Could be set in a menu before starting the game

# What I'd consider internal (private) values in .net
# Prefixing using _ for coding convention 
_won = False
_lost = False
_attempts = 0
_randomNumber = random.randint(cMinNumber, cMaxNumber)

print("Try and guess the random number between " + str(cMinNumber) + " " + str(cMaxNumber)) #Not typed but must cast to concat tho
while not _won and not _lost:
    _attempts += 1

    # prefix processing variables with 'the'
    theGuess = input("Your pick: ")

    if theGuess == str(_randomNumber):
        _won = True
        print(theGuess + " was the correct guess")
    elif _attempts >= cMaxAttempts:
        _lost = True
        print("You lost")
    else:
        print("Guess again. Attemp " + str(_attempts) + " out of " + str(cMaxNumber))

print("End. You could have had a replay option if I wasn't lazy and had it included in another loop.")
