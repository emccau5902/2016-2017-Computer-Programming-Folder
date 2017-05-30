# Add an import statement here so we can use the random.choice function.
import random


# Create a dictionary of 15 Spanish or French words and their English
# translations. Call the dict vocab. 
vocab = {'equipaje' : 'luggage', 'boleto' : 'ticket', 'puerta' : 'gate',
         'vuelo' : 'flight', 'aeropuerto' : 'airport', 'pasajero' : 'passenger',
         'pasaporte' : 'passport', 'pasar por la aduana' : 'to pass through customs',
         'pantalla' : 'screen', 'hacer cola' : 'to get in line',
         'facturar el equipaje' : 'to check ones luggage', 'abordar' : 'board',
         'tomar un taxi' : 'to take taxi', 'agencia de viajes' : 'travel agency',
         'salida' : 'departure', 'parada de autobus' : 'bus stop',
         'pasar de suguridad' : 'to pass through security',
         'auxiliar de vuelo' : 'flight attendant', 'llamar' : 'to call',
         'salir' : 'to leave', 'viajar' : 'to travel', 'llegar' : 'to arrival',
         'donde queda' : 'where is', 'avion' : 'airplane',
         'estacion de tren' : 'train station'}

# Start the game.
print(' _______  ___      _______  _______  __   __    _______  _______  ______    ______   _______ ')
print('|       ||   |    |   _   ||       ||  | |  |  |       ||   _   ||    _ |  |      | |       |')
print('|    ___||   |    |  |_|  ||  _____||  |_|  |  |       ||  |_|  ||   | ||  |  _    ||  _____|')
print('|   |___ |   |    |       || |_____ |       |  |       ||       ||   |_||_ | | |   || |_____ ')
print('|    ___||   |___ |       ||_____  ||       |  |      _||       ||    __  || |_|   ||_____  |')
print('|   |    |       ||   _   | _____| ||   _   |  |     |_ |   _   ||   |  | ||       | _____| |')
print('|___|    |_______||__| |__||_______||__| |__|  |_______||__| |__||___|  |_||______| |_______|')
print("Let's play Flash Cards!")
print('To play, you just type in what the word means in english')
right = 0


# Loop until the player gets 7 consecutive words correct.
while right < 7:
    # Create a list called spanish (or french) which contains the
    # keys from your vocab dict.
    spanish = list(vocab.keys())   

    # Use the choice function to select a random word from the
    # list of keys. Store this word in a variable called question.
    question = random.choice(spanish)

    # Store the corresponding value for that key in a variable
    # called answer.
    answer = vocab[question]

    # Print the question word and prompt the user for a guess.
    guess = input("What does " + question + " mean?")

    # If guess is equal to answer, print a message stating so and
    # increase the right total by 1. Otherwise, print a message
    # telling the player the correct answer and reset right to zero.
    if guess == answer:
        print("You got it right")
        right += 1
    else:
        print("you got it wrong, the answer was " + answer) 
        right = 0
    # Print the number of consecutive correct answers so far.
    print('You have ' + str(right) + ' correct out of 7 needed.')




          
# End the game.
print("Good job. That's 7 correct answers in a row. You win!")
