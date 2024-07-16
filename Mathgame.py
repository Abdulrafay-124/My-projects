import random
import time


OPERATORS = ["+","-","*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
PROBLEMS = 10
wrong = 0 




def generate_problem():
    left = random.randint(MIN_OPERAND,MAX_OPERAND)
    right = random.randint(MIN_OPERAND,MAX_OPERAND)
    operand = random.choice(OPERATORS)

    expr = str(left) + " " + operand + " " + str(right)
    
    answer = eval(expr)
    
    return expr,answer

input("Press Enter to Start! ")
print("----------------------")


start_time = time.time()
for i in range(PROBLEMS):
    expr , answer = generate_problem()
    
    while True:
        guess = input(f"Problem # {i+1} : {expr} = ")
        if guess == str(answer):
            break
        wrong+=1

end_time = time.time()
total_time = end_time - start_time 

print(f"Nice! You finished in {total_time} seconds!  ")
print("-------------------------------------")


    








    
    
 




               

