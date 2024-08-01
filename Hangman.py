import random


print("Hello ! \nWelcome to Hangman.\n Guess the fruit ")
print("You only get 5 guesses")



words = ["apple","mango","banana","watermelon"]

secret_word = random.choice(words)
blanks = []
guesses = 0
for letter in secret_word:
    blanks += "_"


print(blanks)

game_over = False

while not game_over:
    guess = input("guess a letter : ").lower()

    for position in range(len(secret_word)):
        
        letter = secret_word[position]
        
        if letter == guess:
            blanks[position] = letter
    if guess not in secret_word:
        guesses += 1
        guesses_left = 5 - guesses
        print(f"You only have {guesses_left} guesses left")
        if guesses >= 5:
            print("You lost ! ")
            game_over = True
    print(blanks)        
    if "_" not in blanks:
        print("You win")
        game_over = True
