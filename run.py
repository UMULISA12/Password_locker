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
   
    while True:

       print("Hello Welcome password locker!!")
       # user_name = input()
       # print(f"Hello {user_name}. what would you like to do?")
       print('\n')
       print("Use these short codes: Create new user 'cu': Login to your account 'ex' -exit password locker")
       short_code = input().lower()


    if short_code == 'cu':

             print("Enter first name:")
             created_user_name = input()

             print("Enter last name:")
             created_user_name = input()

             print("Enter username:")
             created_user_name = input()

             print("Select a Password:")
             print("-"*5)
             created_user_password = input()

             print("Confirm your password!")
             confirm_password = input()


    else:
            print("Login to your account:")
            print("Enter your username:")
            username = input()
            print("Enter your password:")
            password = input()

    else:
        print('/n')
        print("Use this short codes: View your credentials 'vi'  Add new credential 'add'  Delete credential 'del'  Search credential 'sear'")
        print('/n')
        short-code = input()

     if short-code == 'add':
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
