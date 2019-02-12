#!/usr/bin/env python3.6

from credential import Credentials
from user import Users



#create new credential

def create_credential(site_name,site_username,site_userpassword):
    '''
    Function to create a new credential
    '''
    new_credential = Credentials(site_name,site_username,site_userpassword)
    return new_credential


def save_credentials(credential):
    '''
    Function to save credential
    '''
    credential.save_credential()


def del_credential(credential):
    '''
    Function to delete a credential
    '''
    credential.delete_credential()


def find_credential(site):
    '''
    Function that finds a credential by site_name and returns the credential
    '''
    return Credentials.find_by_site_name(site)


def check_existing_credentials(name):
    '''
    Function that check if a contact exists with that number and return a Boolean
    '''
    return Credentials.find_by_site_name(name)


def display_credentials():
    '''
    Function that returns all the saved contacts
    '''
    return Credentials.display_credentials()


def main():

    print("Hello Welcome password locker!. What is your name?")
    user-name = input()

    print(f"Hello {user-name}. what would you like to do?")
    print('\n')
     
    while True:

    #    print("Hello Welcome password locker!!")
    #    # user_name = input()
    #    # print(f"Hello {user_name}. what would you like to do?")
    #    print('\n')

       print("Use these short codes: 'cu' Create new user  'la' Login to your account  'ex' exit")
       short_code = input().lower()


    if short_code == 'cu':

             print("Enter first name:")
             created_fname = input()

             print("Enter last name:")
             created_lname = input()

             print("Enter username:")
             created_user_name = input()

             print("Select a Password:")
             print("-"*5)
             created_user_password = input()

             print("Confirm your password!")
             confirm_password = input()


             save_users(create_users(created_fname,created_lname,created_user_name,created_user_password)) # create and save new credential.
             print ('\n')
             print(f"new user {created_fname} {created_lname} created an account!")
             print ('\n')


    elif short_code == 'la':

        print("Login to your account:")
        print("Enter your username:")
        username = input()
        print("Enter your password:")
        password = input()


        if username != created_user_name or password != created_user_password:
            print("You entered a wrong username or password")
            print("Username")
            username = input()
            print("Your Password")


        else:
            print('/n')
            print("Use this short codes: View your credentials 'vi'  Add new credential 'add'  Delete credential 'del'  Search credential 'sear'")
            print('/n')
            short-code = input()

    elif short-code == 'add':
        print("Enter site name:")
        site_name = input()
        print("Enter a password:")
        password = input()

    elif short-code == 'vi':
                        
      while True:
          print("This is the list of your credentials")
          if display_credentials():

            for credential in display_credentials():
            print(f"site name:{credential.site_name}")
            print(f"site password:{credential.password}")

    else:
         print('\n')
         print("You don't seem to have any credentials yet")
         print('\n')

         print("Enter the number you want to search for")

            search_credential = input()
            if check_existing_credentials(search_number):
                search_credential = find_credential(search_credential)
                print(f"{search_credential.site_name {search_contact.site_username}")
                print('-' * 20)

                print(f"site user password.......{search_credential.site_userpassword}")
                # print(f"Email address.......{search_contact.email}")
            else:
                print("That credential does not exist")

         elif short_code == "ex":
                print("Bye .......")
                break
         else:
                print("I really didn't get that. Please use the short codes")  
