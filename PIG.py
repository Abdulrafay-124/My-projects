import random

Winning_score = 50

player_scores = [0,0]
current_turn_score = 0
current_player = 0

def roll_die():
    return random.randint(1,6)

def player_decision():
    while True:
        decision = input("Enter r to roll or h to hold: ").lower()
        if decision in ['r' , 'h']:
            return decision
        else:
            print("Invalid input!")

def player_turn(player):
    global current_turn_score
    while True:
        decision = player_decision()
        if decision == 'r':
            roll = roll_die()
            print(f"Player {player + 1} rolled a {roll}.")
            if roll == 1:
                print("Rolled a 1 , no points this turn.")
                current_turn_score = 0
                return
            else:
                current_turn_score += roll
                print(f"Current turn score is {current_turn_score}.")
        elif decision == 'h':
            player_scores[player] += current_turn_score
            print(f"Player {player + 1 } holds . Total score {player_scores[player]}")
            current_turn_score = 0
            return

def check_winner():
    for i , score in enumerate(player_scores):
        if score >= Winning_score:
            print(f"Player {i + 1} wins with a score of {score}")
            return True
    return False


def main():
    global current_player
    print("Welcome to Pig game.")

    while True:
        print(f"Player {current_player + 1}'s turn.")
        player_turn(current_player)
        if check_winner():
            break
        current_player = 1 - current_player

if __name__ == '__main__':
    main()





















