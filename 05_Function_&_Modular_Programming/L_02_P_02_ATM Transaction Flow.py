amount = 0

def show_menu():
    value = int(input("Enter 0 for exit\n1 for check_balance\n2 for deposit\n3 for withdraw\n=> "))

    if value == 0:
        exit_atm()
    elif value == 1:
        check_balance()
    elif value == 2: 
        deposit()
    elif value == 3:
        withdraw()
    else:
        print("You enter wrong command!")
        show_menu()


def exit_atm():
    print("You exit the ATM")



def check_balance():
    print("Your balance is: ", amount)

    value = int(input("Enter 0 for exit\n1 for go back manue\n=> "))
    if value == 0: 
        exit_atm()
    elif value == 1: 
        show_menu()
    else: 
        print("you enter wrong command!")
        check_balance()

def deposit():
    global amount
    value = int(input("Welcome here for deposit\nHow much you want to deposit\n=> "))

    if value <= 0:
        print("please enter valid number!")
        deposit()
    else: 
        amount += value
        print("Congratulations! deposit successful.\n ", check_balance())

def withdraw():
    global amount
    value = int(input("How much you want to withdraw?\n=> "))

    if amount == value: 
        ans = int(input("Are you sure your balance will be 0!\nIf yes then 1\nNo then 0"))
        if ans == 0:
            withdraw()
        elif ans == 1:
            amount = amount - value
            print("Withdraw successful!")
        else: 
            print("You enter wrong command!")
            withdraw()
    elif amount < value: 
        print("You do not have sufficiand money!\n", check_balance())
    else:
        amount = amount - value
        print("Withdraw successful!")
        do = int(input("Enter 0 for exit\n1 for go back manue\n=> "))
        if do == 0: 
            exit_atm()
        elif do == 1: 
            show_menu()


show_menu()