import random
import math

def start_screen():
    print("************************")
    print("*                      *")
    print("*    Guess-A-Number!   *")
    print("*                      *")
    print("* Press ENTER to play. *")
    print("*                      *")
    print("************************")
    input()
    
def play():

    low = 1
    high = 100
    limit = int(math.log(high - low, 2)) + 1
    tries = 0

    print("I'm thinking of a number from " + str(low) + " to " + str(high) + ".")
    print("You try to guess, and I'll tell you if you're right.")
    print("You have " + str(limit) + " attempts to get it.")
    
    num = random.randint(low, high)

    got_it = False
    
    while got_it == False and tries < limit:
        
        guess = input("What number am I thinking of? ")
        guess = int(guess)
        
        if guess < num:
            print("Nope. Your guess is too low.")
        elif guess > num:
            print("Nope. Your guess is too high.")
        else:
            got_it = True

        tries += 1
        print()

    if got_it == True:
        print("You're a winner!")
    else:
        print("You r dum")
    print()


def play_again():

    while True:
        answer = input("Would you like to play again? ")

        if answer == 'no' or answer == 'n':
            return False
        elif answer == 'yes':
            return True

        print("What?!!! Just say yes or no.")


# game begins
start_screen()

again = True

while again == True:
    play()
    again = play_again()
    
print("Game over")








