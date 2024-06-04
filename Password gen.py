master_pwd = input("Enter the master password : ").lower()
if master_pwd == 'rafay':
    print("Welcome!")
else:
    print("wrong! try again")


def view():
    with open("password.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print('User:', user, "| Password:", passw)


def add():

    user = input("Enter Account Name: ")
    pwd = input("Enter Password : ")
    with open('password.txt','a') as f:
        f.write(user + "|" + pwd + "\n")


while True:
    options = input("Do you want to view or add passwords ? (view/add) or q to quit: ").lower()
    if options == "q":
        break
    if options == "view":
        view()
    elif options == "add":
        add()
    else:
        print("Not A Valid Option!")
        continue