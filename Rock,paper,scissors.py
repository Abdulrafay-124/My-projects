import random

print("Welcome!")
choices = ['rock','paper','scissors']
player_score = 0
pc_score = 0


while True:
    player_choice = input("Choose your option: rock , paper , scissors or quit(q); ").lower()

    if player_choice == "q":
        break
    if player_choice not in choices:
        print("Choose something valid ! ")
        continue

    random_number = random.randint(0,2)
    # Here 0 is for ROCK , 1 is for PAPER and 2 is for Scissors respectively.

    computer_choice = choices[random_number]
    print("The computer chose", computer_choice + ".")

    if player_choice == 'rock' and computer_choice == 'scissors':
        print("You Win !")
        player_score += 1
    elif player_choice == 'paper' and computer_choice == 'rock':
        print("You Win !")
        player_score += 1
    elif player_choice == 'scissors' and computer_choice == 'paper':
        print("You Win !")
        player_score += 1

    else:
        print("You lose!")
        pc_score += 1
        continue

print(f"Your score is {player_score} "
      f"While pc score is {pc_score}")
print("Thanks for playing")









