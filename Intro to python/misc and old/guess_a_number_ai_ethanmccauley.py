#Guess-A-Number AI
#
#Ethan McCauley
#September 7th, 2016


import random
import math

print("--Before we play, what is your name?--")
name = input()

def start_screen():
    print("   ____                                                     _            ___      ___                         ___                       ")
    print("  6MMMMb/                                                  dM.           `MM\     `M'                          MM                       ")
    print(" 8P    YM                                                 ,MMb            MMM\     M                           MM                       ")
    print("6M      Y ___   ___   ____     ____     ____              d'YM.           M\MM\    M ___   ___ ___  __    __   MM____     ____  ___  __ ")
    print("MM        `MM    MM  6MMMMb   6MMMMb\  6MMMMb\           ,P `Mb           M \MM\   M `MM    MM `MM 6MMb  6MMb  MMMMMMb   6MMMMb `MM 6MM ")
    print("MM         MM    MM 6M'  `Mb MM'    ` MM'    `           d'  YM.          M  \MM\  M  MM    MM  MM69 `MM69 `Mb MM'  `Mb 6M'  `Mb MM69 """)
    print("MM     ___ MM    MM MM    MM YM.      YM.               ,P   `Mb          M   \MM\ M  MM    MM  MM'   MM'   MM MM    MM MM    MM MM'    ")
    print("MM     `M' MM    MM MMMMMMMM  YMMMMb   YMMMMb           d'    YM.         M    \MM\M  MM    MM  MM    MM    MM MM    MM MMMMMMMM MM     ")
    print("YM      M  MM    MM MM            `Mb      `Mb         ,MMMMMMMMb         M     \MMM  MM    MM  MM    MM    MM MM    MM MM       MM     ")
    print(" 8b    d9  YM.   MM YM    d9 L    ,MM L    ,MM         d'      YM.        M      \MM  YM.   MM  MM    MM    MM MM.  ,M9 YM    d9 MM     ")
    print("  YMMMM9    YMMM9MM_ YMMMM9  MYMMMM9  MYMMMM9        _dM_     _dMM_      _M_      \M   YMMM9MM__MM_  _MM_  _MM_MYMMMM9   YMMMM9 _MM_    ")
    print()
def play():
    
    low = 1
    high = 100

    
    got_it = False
    limit = 8
    tries = 1

    
    print("Hello, " + name + ". Please think of a number from " + str(low) + " to " + str(high) + " and I will try to guess it in 7 tries.")
    print("Say if the your number is higher or lower than the guess.")
    input("Press Enter to continue")
    
    while got_it == False and tries < limit:
        guess = (high + low) // 2
        
        print("Is the number " + str(guess) + ", " + name + "?")
        answer = input()

        if answer == 'higher' or answer == 'h':
            low = guess + 1
            tries += 1
        if answer == 'lower' or answer == 'l':
            high = guess - 1
            tries += 1
        if answer == 'yes' or answer == 'y':
            got_it = True
       
    if got_it == True:
        print("Cool I got it in " + str(tries) + " tries.")
    else:
        print("I ran out of guesses")

        
def play_again():
    while True:
        answer = input("Would you like to play again, " + name + "?")

        if answer == 'no' or answer == 'n': 
            return False
    
        elif answer == 'yes' or answer == 'y':
            return True

        print("This was supposed to be a yes/no answer, not a short response.")

start_screen()

again = True
while again == True:
    play()
    again = play_again()

print()
print("Game Over, " + name )
print()
print("-Credits-")
print("Made By Ethan McCauley")
print("Completed on September 7th, 2016.")

