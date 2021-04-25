def account_number_validation(account_number):
    """ This function does the following
    Check if account number is not empty
    Check if account number is 10 digits
    Check if account number is an integer"""
    if account_number:
        try:
            int(account_number)
            if len(str(account_number)) == 10:
                return True
            else:          
                return False
        except ValueError:
            return False  
        except TypeError:
            return False  
    else:
        return False