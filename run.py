from user import User
from credential import Credentials


def acc_name(userName, password):
    '''
    Function to create new account
    '''
    new_user = User(userName, password)
    return new_user


def save_new_user(user):
    '''
    Function to save a user
    '''
    user.save_user()


def account_login(login):
    '''
    Function to login
    '''
    return User.user_login(login)


def create_credentials(acc_name,acc_username,acc_password):
    '''
    Function to create new credential
    '''
    new_credentials = Credentials(acc_name,acc_username,acc_password)
    return new_credentials


def save_user_credentials(credential):
    '''
    Function to save credential
    '''
    credential.save_credentials()


def del_credentials(credential):
    '''
    Function to delete credential from list
    '''
    credential.delete_credentials()


def find_credentials(name):
    '''
    Function that finds a credential by user name and return details
    '''
    return Credentials.find_by_user_name(name)


def copy_username(name):
    return Credentials.copy_username(name)


def check_credentials_exist(name):
    '''
    Function to check if a credential exists
    '''
    return Credentials.credentials_exist(name)


def display_credentials():
    '''
    Function that returns all the saved credential
    '''
    return Credentials.credential_display()


def main():
    print("Welcome to password locker")
    print("Hi welcome to password locker. What's your name?")
    acc_name = input()
    print('\n')

    while True:
        print(f"Please {acc_name}! .Use these short codes: cu-create new user  log-login  ex-exit")
        short_code = input().lower()
        
        if short_code == "cu":
            print("Create account")
            print("_" * 13)
            userName = input()
            print("Choose a password")
            password = input()
            print("_" * 17)
            save_new_user(User(userName, password))
            print(f"""Your user details - Username : {userName} Password : {password}""")
            print("")
            print(f"Hello {userName} please choose from the options below")
            print("")

            while True:
                print("Use these short codes: cc - create new credential, dc - display credential,  exc - exit credential list")
                short_code = input().lower()

                if short_code == 'cc':
                        print("New credential")
                        print("-"*10)

                        print('')

                        print("Account name ...")
                        acc_name = input()

                        print('')

                        print("Accout username ...")
                        acc_username = input()

                        print('')

                        print("Account password")
                        acc_password = input()

                        save_user_credentials(create_credentials(acc_name, acc_username, acc_password))
                        print('')

                        print(f"New credential username : {acc_name}, Account username: {acc_username}")
                        print('')
                elif short_code == 'dc':
                        if display_credentials():
                            print("This is a list of all the credential")
                            print('')
                            for Credentials in display_credentials():
                                print(f"Username : {Credentials.acc_name}, Account username: {Credentials.acc_username} Password : {Credentials.password}")

                                print('')
                        else:
                            print('')
                            print("You have not saved any credential yet")
                            print('')
                elif short_code == "exc":
                        print('')
                        print("Goodbye...... see u")
                        break
                else:
                    print("Please enter a valid short code!")

        elif short_code == "log":
            print("Log in")
            print("please enter a user Name")
            print("_" * 20)
            userName = input()
            print("Enter your password")
            print("_" * 20)

            print(f"Hello {userName} please can you choose from the options below")
            print("")
            while True:
                print("Use these short codes: cc - create new credential, dc - display credential, exc - exit credential list")
                short_code = input().lower()

                if short_code == 'cc':
                        print("New credential")
                        print("-"*10)

                        print('')

                        print("User name ...")
                        acc_name = input()

                        print('')

                        # print("Phone number ...")
                        # phone_number = input()

                        print('')

                        print("Accout username ...")
                        acc_username = input()

                        print('')

                        print("Account password")
                        acc_password = input()

                        save_user_credentials(create_credentials(acc_name, phone_number, acc_username, acc_password))
                        print('')

                        print(f"New credential account : {acc_name}, User name : {phone_number}")
                        print('')
                elif short_code == 'dc':
                        if display_credentials():
                            print("Here is a list of all the credential")
                            print('')
                            for Credentials in display_credentials():
                                print(f"Username : {Credentials.acc_name}, Phone number : {Credentials.phone_number} E-mail address : {Credentials.acc_username} Password : {Credentials.password}")

                                print('')
                        else:
                            print('')
                            print("You have not saved any credential")          
                elif short_code == "exc":
                        print('')
                        print("Bye......see u")
                        break
                else:
                    print("Enter a valid  code")

        elif short_code == "esc":
            print('')
            print("Bye......see u")
            break
        else:
            print("The short code does not  exist")


if __name__ == '__main__':
    
    main() 