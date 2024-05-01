print("Welcome to the quiz game!")

play = input("Do you wish to play ? ")
score = 0

if play == "yes".lower():
    print(" Alright answer these questions! ")
else:
    print("Bye")
    quit()

answer = input("What does PC stand for ? choose (a , b or c) "
               "a.Partition Company      b.Personal Computer  "
               " c.Play Champ : "
               )
if answer == "b":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does CPU stand for ? choose (a , b or c) "
               "a.Cipher Poll Universal       b.Crater Pulled Constantly  "
               " c.Central Processing Unit : "
               )
if answer == "c":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does AI stand for ? choose (a , b or c) "
               "a.Aerospace Integration      b.Asserted Incompetence  "
               " c.Artificial Intelligence : "
               )
if answer == "c":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does LAN stand for ? choose (a , b or c) "
               "a.Local Area Network      b.Leverage and Nesting  "
               " c.Level Air Now : "
               )
if answer == "a":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does NPC stand for ? choose (a , b or c) "
               "a.Non Playable Character      b. Non Paid Character  "
               " c.Not Participating Character  : "
               )
if answer == "a":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print(f"You got {score} out of 5 questions right!")
print(f"{score * 100 / 5 } % of your answers were correct.")

