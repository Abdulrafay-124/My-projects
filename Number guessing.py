import random

top_of_range = input("ENTER A NUMBER: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
else:
    print("Please enter a number next time ! ")
    quit()

random_number = random.randint(0, top_of_range)

guesses = 0



while True:
    guesses += 1
    player_guess = input("Enter your guess: ")
    if player_guess.isdigit():
        player_guess = int(player_guess)
    else:
        print("Enter a number please.")
    if player_guess == random_number:
        print("You guessed the correct number !")
        break
    elif player_guess > random_number:
        print("You guessed too high ! ")

    elif player_guess < random_number:
        print("You guessed too low ! ")

    else:
        print("Invalid !")
        break
print("You made",guesses,"guesses." )






