print("Welcome to Death Trail ! ")
answer = input("You woke up feeling nauseous,"
               " \nDo you take a pill next to your bed for headache or go on with your day(YES/NO): ").lower()
if answer == 'yes':
    answer = input("You start feeling better and get a move on ,"
                   "\nThe death trail awaits you, You pack your bags and leave the house."
                   "\nYou come across an intersection which path will you take ? (left/right): ").lower()
    if answer == 'left':
        answer = input("You went left , it lead to a jungle,"
                       "\nyou feel terror creep down your spine , will you return (yes/no): ").lower()
        if answer == "yes":
            print("You chose to return and lived your life peacefully coward ! you lost :(")
        elif answer == "no":
            print("You doomed yourself , as soon as you entered the jungle you got shredded to pieces "
                  "\nCongratulations! you Won ! Happy Dying :)")

    elif answer == 'right':
        answer = input("Looks like this is the right path the snakes hissing, wolves howling indicate so "
                       "\nThis is what you wanted ! Death Trail leads to only one outcome."
                       "\nNO backing down now! (sure/no way): ").lower()
        if answer == 'sure':
            print("You got massacred in the most deplorable way , \nCongrats! YOU WON Dude.")
            quit()
        elif answer == 'no way':
            print("You ran for your life, lived the rest of life back on your farmhouse ,"
                  "\nit was a lovely life , but you regretted not walking the Death trail your whole life ! ")
    else:
        print("Write something valid next time.")
elif answer == 'no':
    print("You start to feel dizzy and pass out , GAME OVER.")

else:
    print("Write something valid")

print("Thanks for Playing ! ")
