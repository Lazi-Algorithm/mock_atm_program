"""
    AN IMPROVED MOCKUP ATM PROGRAM WRITTEN IN PYTHON

    This program contains the following operations
    1. Register - [firstname, lastname, password, email]
    2. Login - [account number, password]
    3. bank Operations - [Deposit, withdraw, transfer, checkbalance]

"""

import random #for random number generation
import time 
import validation
import database
from getpass import getpass

#initializing function
def init():
    print("Welcome to Zuri Bank ATM")
    time.sleep(2)
    have_account = input("Do you have an account with us: yes (1) No (2) ==> ")
    try:
        int(have_account)
        
    except ValueError:
        print("[INFO]: Invalid option Selected. Try again")
        init()
    have_account = int(have_account)
    if have_account == 1:
        login()
    elif have_account == 2:
        register()
    else:
        print("You selected an invalid option! try again")
        init()
        
def login():
    print("~~~~~~~~LOGIN~~~~~~~~~~")
    print("Enter your account number.")
    user_acc_num = input("Account Number:==>\t")
    time.sleep(1)
    is_account_number_valid = validation.account_number_validation(user_acc_num)
    if is_account_number_valid:
        account_exits = database.does_account_number_exist(user_acc_num)
        if account_exits:
            details = database.read(user_acc_num)
            name = details[0]
            time.sleep(1)
            print("Welcome {} to Zuri Bank ATM".format(name))
            time.sleep(1)
            invalid_pin = True
            trial = 1
            while invalid_pin == True:
                print("Enter your four digit pin")
                pin = int(getpass("Pin:==>\t "))
                
                if pin == int(details[3]):
                    print("Pin Correct!")
                    time.sleep(1)
                    bank_operations(user_acc_num)
                    invalid_pin = False
                    user_details = details
                else:
                    if trial <= 3:
                        print("Incorrect pin! Try again. You have {} trial left".format(3-trial))
                    else:
                        print("Exceeded Pin Trial! CARD BLOCKED!")
                        print("CLosing program....")
                        time.sleep(2)
                        init()
                    trial += 1
        else:    
            print("[INFO]: No Record Found! Try again")
            login()
    else:
        print("[INFO]: Account number invalid")
        init()
    return user_details
    
def register():
    print("Thank you for choosing us. \n Enter the following details:")
    firstname = input("Firstname : ")
    lastname = input("Lastname : ")
    email = input("Email Address : ")
    pin = int(input("Choose a Four Digit Pin: "))
    opening_balance = int(input("How much do you want to deposit initially?: "))
    account_number = generate_account_number()
    
    is_user_created = database.create(account_number, firstname, lastname, email, pin, opening_balance)
    if is_user_created:
        print("processing...")
        time.sleep(1)
        print("Congratulations!!! Your account is created. \nHere is your account number:\t {}".format(account_number))
        time.sleep(1)
        login()
    else:
        print("[INFO]: Something went wrong, please try again!")
        register()

def generate_account_number():
    account_number = random.randrange(1111111111, 9999999999)
    return account_number

    
def withdrawal(user_acc_num):
    details = database.read(user_acc_num)
    balance = int(details[-1])
    withdraw_amount = int(input("How much do you want to withdrawal? ==> "))
    print("Please wait while your transaction is processing...")
    time.sleep(2)
    if withdraw_amount > balance:
        print("[INFO]: Insufficient Funds. Try again")
        bank_operations(user_acc_num)
    else:
        print("[INFO]: Withdraw successfull. Take your cash")
        new_balance = balance - withdraw_amount
        details[-1] = new_balance
        database.update(user_acc_num, details)
        print("Your new account balance is %d" %new_balance)
    
    bank_operations(user_acc_num)

def deposit(user_acc_num):
    details = database.read(user_acc_num)
    balance = int(details[-1])
    deposit_amount = input("How much do you want to withdraw? ==> ")
    try:
        int(deposit_amount)
    except ValueError:
        print("[INFO]:Invalid Amount Selection. Try again!")
        deposit()
    print("[INFO]: Processing...")
    time.sleep(1)
    new_balance = balance + withdraw_amount
    details[-1] = new_balance
    database.update(user_acc_num, details)
    print("Your new account balance is %d" %new_balance)
    option = int(input("Press 1. Exit or 2. to go back\t ==> "))
    if option == 1:
        exit()
    elif option == 2:
        bank_operations(user_acc_num)
    else:
        print("Invalid option selected. Going back to previous menu")
        time.sleep(1)
        bank_operations(user_acc_num)

def bank_operations(user_acc_num):
    print("What do you want to do?")
    choice = input(" 1. Withdrawal \n 2. Deposit\n 3. Logout\n 4. Exit\n ==>>" )
    try:
        int(choice)
    except ValueError:
        print("[INFO]:Invalid Selection. Try again!")
        bank_operations()
    choice = int(choice)
    if choice == 1:
        withdrawal(user_acc_num)
    elif choice == 2:
        deposit(user_acc_num)
    elif choice == 3:
        login()
    elif choice == 4:
        exit()
    else:
        print("[INFO]: Incorrect option selected. Try again")
        bank_operations()
    



init()