#CRUD Operations
#create record
#read record
#update record
#delete record

import os
import validation
user_db_path = "database/user_record/"

    

def create(user_account_number, firstname, lastname, email, pin, opening_balance):
    print("create a new user record")
    #Create a file named account_number.txt and add user details to the file
    #return true
    completed = False
    user_details = firstname + "," + lastname + "," + email + "," + str(pin) + "," + str(opening_balance)
    if does_account_number_exist(user_account_number):
        return False
    if does_email_exist(email):
        print("[INFO]: User already exist. please login or try again")
        return False
    try:
        f = open("database/user_record/" + str(user_account_number) + ".txt", "x")        
    except FileExistsError:
        does_user_exist = read("database/user_record/" + str(user_account_number) + ".txt", "x")
        if not does_user_exist:
            delete(user_account_number)
        print("User already exits")
        
        #delete(account_number)
    else:
        f.write(str(user_details))
        completed = True
        
    finally:    
        f.close()
    return completed
    

def read(user_account_number):
    is_valid_acc_num = validation.account_number_validation(user_account_number)
    
    try:
        if is_valid_acc_num:
            user_file = user_db_path + str(user_account_number) + ".txt"
        else:
            user_file = user_db_path + user_account_number
        f = open(user_file, "r")
        record = f.readline()
        record = str.split(record, ',')
    except FileNotFoundError:
        print("[INFO]: User not Found")
    except FileExistsError:
        print("[INFO]: User do not Exist")
    except TypeError:
        print("[INFO]: Invalid account number")
    else:
        return record



def update(user_account_number, details):
    print(details)
    print("Update User record")
    #find user with account number
    #fetch content of file
    #update the content of the file
    #save the file
    #return true

def delete(user_account_number):
    print("delete user record")
    #find user account number
    #delete the file
    is_delete_success = False
    user_file = user_db_path + str(user_account_number) + ".txt"
    try:
        os.remove(user_file)
        is_delete_success = True
    except FileNotFoundError:
        print("user not found")
    finally:
        return is_delete_success


def does_email_exist(email):
    all_user_records = os.listdir(user_db_path)
    for user in all_user_records:
        record = read(user)
        record = str.split(record, ',')
        if email in record:
            return True
        else:
            return False
        

def does_account_number_exist(user_account_number):
    all_user_records = os.listdir(user_db_path)
    for user in all_user_records:
        if user == str(user_account_number) + ".txt":
            return True
        else:
            return False 

#create(1234567891, ["eloghosa", "ikponmwoba", "elotechy@gmail.com", 1111])
# print(read("3465488108"))
#print(does_account_number_exist(1234567891))