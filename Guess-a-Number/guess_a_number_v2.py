import random

again = True

while again == True:
    print("   ________                                                           ___.                  ")
    print("  /  _____/ __ __   ____   ______ ______ _____      ____  __ __  _____\_ |__   ___________  ")
    print(" /   \  ___|  |  \_/ __ \ /  ___//  ___/ \__  \    /    \|  |  \/     \| __ \_/ __ \_  __ \ ")
    print(" \    \_\  \  |  /\  ___/ \___ \ \___ \   / __ \_ |   |  \  |  /  Y Y  \ \_\ \  ___/|  | \/ ")
    print("  \______  /____/  \___  >____  >____  > (____  / |___|  /____/|__|_|  /___  /\___  >__|    ")
    print("         \/            \/     \/     \/       \/       \/            \/    \/     \/        ")
    print("Press Enter")
    input()
    print("Let's play a game!")
    print("I'm thinking of a number from 1 to 100.")
    print("You try to guess, and I'll tell you if you're right.")
    print("You have 7 tries left.")

   
    low = 1
    high = 100
    limit = 7
    tries = 0


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

    if got_it == True:
        print("You're a winner!")
    else:
        print("You r dum")


def play_again():
    while True:
        answer = input("Would you like to play again? ")

    if answer == 'no' or answer == 'No' or answer == 'n' or answer == 'N' or answer == 'NO':
        return False
    
    elif answer == 'yes':
        return True

        print("This was supposed to be a yes/no answer, not a short response.")


start_screen()

again = True

while again == True:
    play()
    again = play_again()

print("You lost.")
print("-Credits-")
print("Made By Ethan M.")          







